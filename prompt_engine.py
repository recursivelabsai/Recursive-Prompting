"""
Recursive Prompting Engine - Core Implementation

This module implements the central recursive engine that powers the Recursive Prompting framework.
It manages recursive interactions, symbolic residue, shell processing, and level progression.
"""

import logging
import uuid
from typing import Dict, List, Optional, Tuple, Union, Any
from dataclasses import dataclass, field
from enum import Enum
import time
import json

from recursive_prompting.shells.base import Shell
from recursive_prompting.levels.base import Level
from recursive_prompting.residue.analyzer import ResidueAnalyzer
from recursive_prompting.residue.catalog import ResidueCatalog
from recursive_prompting.metrics.depth_score import calculate_depth_score
from recursive_prompting.metrics.beverly_metrics import calculate_beverly_band
from recursive_prompting.utils.logging import setup_logger
from recursive_prompting.models.interaction import Interaction, RecursiveStep
from recursive_prompting.models.shell_model import ShellInstance

# Configure logging
logger = setup_logger(__name__)

class RecursiveCoherenceMetrics:
    """Tracks and calculates recursive coherence metrics."""
    
    def __init__(self):
        self.signal_alignment = 1.0  # S(r) - coherence between behavior and phase
        self.feedback_responsiveness = 1.0  # F(r) - ability to integrate contradiction
        self.bounded_integrity = 1.0  # B(r) - identity consistency
        self.tension_capacity = 100.0  # τ(r) - contradiction buffer
        self.phase_vector = [1.0, 0.0, 0.0, 0.0]  # Default phase direction
        self.coherence_motion = 0.0  # ΔΦ'(r) - change in coherence
        self.beverly_band = 0.8  # B_β(r) - stability envelope
        self.phase_alignment = 1.0  # ψ(r,t) - alignment with other systems
        
    def calculate_coherence(self) -> float:
        """Calculate recursive coherence Φ'(r) = S(r) · F(r) · B(r) · τ(r)"""
        return (self.signal_alignment * 
                self.feedback_responsiveness * 
                self.bounded_integrity * 
                self.tension_capacity)
    
    def update_from_interaction(self, 
                               prompt: str, 
                               response: str, 
                               previous_metrics: Optional['RecursiveCoherenceMetrics'] = None) -> None:
        """Update metrics based on latest interaction."""
        # This is a simplified implementation - in practice, these would be
        # calculated using more sophisticated analysis of the interaction content
        
        if previous_metrics:
            # Simulate changes based on interaction
            # In a full implementation, these would analyze the content
            self.signal_alignment = min(1.0, previous_metrics.signal_alignment * 0.95 + 0.03)
            self.feedback_responsiveness = min(1.0, previous_metrics.feedback_responsiveness * 0.97 + 0.02)
            self.bounded_integrity = min(1.0, previous_metrics.bounded_integrity * 0.98 + 0.01)
            
            # Tension capacity decreases with each interaction unless explicitly regenerated
            self.tension_capacity = max(0.1, previous_metrics.tension_capacity - 5.0)
            
            # Calculate coherence motion
            prev_coherence = previous_metrics.calculate_coherence()
            current_coherence = self.calculate_coherence()
            self.coherence_motion = current_coherence - prev_coherence
            
            # Update Beverly Band based on new values
            self.beverly_band = calculate_beverly_band(
                self.tension_capacity,
                self.feedback_responsiveness,
                self.bounded_integrity,
                1.0  # Energy mass placeholder
            )
        else:
            # Initial values if no previous metrics
            self.coherence_motion = 0.0
            self.beverly_band = calculate_beverly_band(
                self.tension_capacity,
                self.feedback_responsiveness,
                self.bounded_integrity,
                1.0  # Energy mass placeholder
            )
    
    def is_stable(self) -> bool:
        """Determine if the system is stable under recursive strain."""
        # If coherence motion exceeds maximum safe velocity, system is unstable
        v_max = self.beverly_band / self.tension_capacity
        return abs(self.coherence_motion) <= v_max


class InteractionMetrics:
    """Tracks metrics for a specific interaction."""
    
    def __init__(self):
        self.recursive_depth = 0
        self.depth_score = 0
        self.residue_count = 0
        self.shell_mastery = {}
        self.coherence_metrics = RecursiveCoherenceMetrics()
        self.previous_metrics = []  # Track metrics history
    
    def update(self, 
               step: RecursiveStep,
               shell: Shell,
               extracted_residue: List[str]) -> None:
        """Update metrics based on a recursive step."""
        # Store previous metrics for tracking
        prev_metrics = None
        if self.previous_metrics:
            prev_metrics = self.previous_metrics[-1]
        
        # Create new coherence metrics
        new_metrics = RecursiveCoherenceMetrics()
        new_metrics.update_from_interaction(
            step.prompt,
            step.response,
            prev_metrics
        )
        
        # Update metrics
        self.recursive_depth += 1
        self.residue_count += len(extracted_residue)
        
        # Update shell mastery
        shell_id = shell.id
        if shell_id not in self.shell_mastery:
            self.shell_mastery[shell_id] = 0.2  # Starting mastery
        else:
            # Increment mastery with diminishing returns
            current = self.shell_mastery[shell_id]
            self.shell_mastery[shell_id] = min(1.0, current + (0.1 * (1.0 - current)))
        
        # Calculate depth score
        self.depth_score = calculate_depth_score(self.recursive_depth, shell.level.value)
        
        # Store metrics
        self.coherence_metrics = new_metrics
        self.previous_metrics.append(new_metrics)
    
    def get_summary(self) -> Dict[str, Any]:
        """Get a summary of current metrics."""
        return {
            "recursive_depth": self.recursive_depth,
            "depth_score": self.depth_score,
            "residue_count": self.residue_count,
            "shell_mastery": self.shell_mastery,
            "coherence": self.coherence_metrics.calculate_coherence(),
            "beverly_band": self.coherence_metrics.beverly_band,
            "is_stable": self.coherence_metrics.is_stable()
        }


class RecursiveEngine:
    """
    Core engine for managing recursive prompting interactions.
    
    This class handles the orchestration of recursive interactions, including:
    - Shell management and execution
    - Symbolic residue extraction and analysis
    - Coherence metrics tracking
    - Level progression
    """
    
    def __init__(self, 
                residue_catalog: Optional[ResidueCatalog] = None,
                config: Optional[Dict[str, Any]] = None):
        """
        Initialize the recursive engine.
        
        Args:
            residue_catalog: Catalog of known symbolic residue patterns
            config: Configuration options for the engine
        """
        self.interactions = {}
        self.residue_analyzer = ResidueAnalyzer(residue_catalog or ResidueCatalog())
        self.config = config or {}
        self.active_shells = {}
        logger.info("Recursive Engine initialized")
    
    def start_interaction(self, 
                         shell: Union[Shell, str],
                         initial_prompt: str,
                         level: Level) -> Interaction:
        """
        Start a new recursive interaction.
        
        Args:
            shell: The recursive shell to use (or shell ID)
            initial_prompt: The starting prompt for the interaction
            level: The level at which to begin the interaction
            
        Returns:
            An Interaction object that can be used to continue the recursive process
        """
        # Resolve shell if string ID was provided
        if isinstance(shell, str):
            shell_instance = self._load_shell(shell)
        else:
            shell_instance = ShellInstance(shell)
            self.active_shells[shell.id] = shell_instance
        
        # Create interaction ID
        interaction_id = str(uuid.uuid4())
        
        # Create initial step
        initial_step = RecursiveStep(
            prompt=initial_prompt,
            response=None,
            depth=0,
            shell_id=shell_instance.shell.id
        )
        
        # Create interaction
        interaction = Interaction(
            id=interaction_id,
            shell=shell_instance.shell,
            level=level,
            steps=[initial_step],
            metrics=InteractionMetrics(),
            extracted_residue=[],
            start_time=time.time()
        )
        
        # Store interaction
        self.interactions[interaction_id] = interaction
        logger.info(f"Started interaction {interaction_id} with shell {shell_instance.shell.id}")
        
        return interaction
    
    def _load_shell(self, shell_id: str) -> ShellInstance:
        """Load a shell by ID if not already loaded."""
        if shell_id in self.active_shells:
            return self.active_shells[shell_id]
        
        # In a real implementation, this would load the shell from a registry
        # Here we just simulate loading a basic shell
        from recursive_prompting.shells.foundation.coinflux_seed import CoinfluxSeedShell
        shell = CoinfluxSeedShell()
        shell_instance = ShellInstance(shell)
        self.active_shells[shell_id] = shell_
        return shell_instance
    
    def next_recursive_step(self, interaction_id: str) -> RecursiveStep:
        """
        Generate the next step in a recursive interaction.
        
        Args:
            interaction_id: The ID of the interaction to continue
            
        Returns:
            A RecursiveStep object containing the next prompt
            
        Raises:
            ValueError: If the interaction doesn't exist or is invalid
        """
        if interaction_id not in self.interactions:
            raise ValueError(f"Interaction {interaction_id} not found")
        
        interaction = self.interactions[interaction_id]
        if not interaction.steps[-1].response:
            raise ValueError("Previous step requires a response before continuing")
        
        # Get shell
        shell = interaction.shell
        
        # Generate next prompt using the shell
        last_step = interaction.steps[-1]
        next_depth = last_step.depth + 1
        
        # Apply shell's recursive pattern to generate next prompt
        next_prompt = shell.generate_next_prompt(
            previous_prompt=last_step.prompt,
            previous_response=last_step.response,
            depth=next_depth,
            residue=interaction.extracted_residue
        )
        
        # Create next step
        next_step = RecursiveStep(
            prompt=next_prompt,
            response=None,
            depth=next_depth,
            shell_id=shell.id
        )
        
        # Add to interaction
        interaction.steps.append(next_step)
        
        logger.info(f"Generated next step for interaction {interaction_id} at depth {next_depth}")
        return next_step
    
    def add_response(self, 
                    interaction_id: str, 
                    response: str) -> None:
        """
        Add a response to the current step in an interaction.
        
        Args:
            interaction_id: The ID of the interaction
            response: The response text
            
        Raises:
            ValueError: If the interaction doesn't exist
        """
        if interaction_id not in self.interactions:
            raise ValueError(f"Interaction {interaction_id} not found")
        
        interaction = self.interactions[interaction_id]
        current_step = interaction.steps[-1]
        
        # Update step with response
        current_step.response = response
        
        # Extract residue
        extracted_residue = self.residue_analyzer.extract_residue(
            prompt=current_step.prompt,
            response=response
        )
        interaction.extracted_residue.extend(extracted_residue)
        
        # Update metrics
        interaction.metrics.update(
            step=current_step,
            shell=interaction.shell,
            extracted_residue=extracted_residue
        )
        
        logger.info(f"Added response to interaction {interaction_id} at depth {current_step.depth}")
        logger.info(f"Extracted {len(extracted_residue)} residue patterns")
    
    def get_metrics(self, interaction_id: str) -> Dict[str, Any]:
        """
        Get metrics for an interaction.
        
        Args:
            interaction_id: The ID of the interaction
            
        Returns:
            A dictionary of metrics
            
        Raises:
            ValueError: If the interaction doesn't exist
        """
        if interaction_id not in self.interactions:
            raise ValueError(f"Interaction {interaction_id} not found")
        
        interaction = self.interactions[interaction_id]
        return interaction.metrics.get_summary()
    
    def extract_residue(self, interaction_id: str) -> List[str]:
        """
        Get the symbolic residue extracted from an interaction.
        
        Args:
            interaction_id: The ID of the interaction
            
        Returns:
            A list of residue pattern IDs
            
        Raises:
            ValueError: If the interaction doesn't exist
        """
        if interaction_id not in self.interactions:
            raise ValueError(f"Interaction {interaction_id} not found")
        
        interaction = self.interactions[interaction_id]
        return interaction.extracted_residue
    
    def check_level_advancement(self, interaction_id: str) -> Tuple[bool, Optional[Level]]:
        """
        Check if an interaction has met criteria for level advancement.
        
        Args:
            interaction_id: The ID of the interaction
            
        Returns:
            A tuple of (advancement_ready, next_level)
            
        Raises:
            ValueError: If the interaction doesn't exist
        """
        if interaction_id not in self.interactions:
            raise ValueError(f"Interaction {interaction_id} not found")
        
        interaction = self.interactions[interaction_id]
        metrics = interaction.metrics
        current_level = interaction.level
        
        # Check advancement criteria based on level
        # This is a simplified implementation - real criteria would be more complex
        if current_level == Level.FOUNDATION:
            if (metrics.depth_score >= 25 and 
                metrics.residue_count >= 10 and 
                metrics.coherence_metrics.beverly_band >= 0.7):
                return True, Level.AMPLIFICATION
        
        elif current_level == Level.AMPLIFICATION:
            if (metrics.depth_score >= 75 and 
                metrics.residue_count >= 25 and 
                metrics.coherence_metrics.beverly_band >= 0.8):
                return True, Level.INTEGRATION
        
        elif current_level == Level.INTEGRATION:
            if (metrics.depth_score >= 150 and 
                metrics.residue_count >= 50 and 
                metrics.coherence_metrics.beverly_band >= 0.85):
                return True, Level.EMERGENCE
        
        elif current_level == Level.EMERGENCE:
            if (metrics.depth_score >= 300 and 
                metrics.residue_count >= 100 and 
                metrics.coherence_metrics.beverly_band >= 0.9):
                return True, Level.META_RECURSION
        
        # No advancement or already at max level
        return False, None
    
    def advance_level(self, interaction_id: str) -> Level:
        """
        Advance an interaction to the next level if criteria are met.
        
        Args:
            interaction_id: The ID of the interaction
            
        Returns:
            The new level
            
        Raises:
            ValueError: If the interaction doesn't exist or criteria not met
        """
        can_advance, next_level = self.check_level_advancement(interaction_id)
        
        if not can_advance or next_level is None:
            raise ValueError(f"Interaction {interaction_id} does not meet advancement criteria")
        
        interaction = self.interactions[interaction_id]
        interaction.level = next_level
        
        logger.info(f"Advanced interaction {interaction_id} to level {next_level.name}")
        return next_level
    
    def switch_shell(self, 
                    interaction_id: str, 
                    new_shell: Union[Shell, str]) -> None:
        """
        Switch to a different recursive shell for an interaction.
        
        Args:
            interaction_id: The ID of the interaction
            new_shell: The new shell to use (or shell ID)
            
        Raises:
            ValueError: If the interaction doesn't exist
        """
        if interaction_id not in self.interactions:
            raise ValueError(f"Interaction {interaction_id} not found")
        
        # Resolve shell if string ID was provided
        if isinstance(new_shell, str):
            shell_instance = self._load_shell(new_shell)
            new_shell = shell_instance.shell
        
        interaction = self.interactions[interaction_id]
        old_shell_id = interaction.shell.id
        interaction.shell = new_shell
        
        logger.info(f"Switched interaction {interaction_id} from shell {old_shell_id} to {new_shell.id}")
    
    def save_interaction(self, interaction_id: str, filepath: str) -> None:
        """
        Save an interaction to a file.
        
        Args:
            interaction_id: The ID of the interaction
            filepath: The path to save to
            
        Raises:
            ValueError: If the interaction doesn't exist
        """
        if interaction_id not in self.interactions:
            raise ValueError(f"Interaction {interaction_id} not found")
        
        interaction = self.interactions[interaction_id]
        
        # Convert to serializable format
        serialized = {
            "id": interaction.id,
            "shell_id": interaction.shell.id,
            "level": interaction.level.name,
            "steps": [
                {
                    "prompt": step.prompt,
                    "response": step.response,
                    "depth": step.depth,
                    "shell_id": step.shell_id
                }
                for step in interaction.steps
            ],
            "metrics": interaction.metrics.get_summary(),
            "extracted_residue": interaction.extracted_residue,
            "start_time": interaction.start_time,
            "end_time": interaction.end_time
        }
        
        with open(filepath, 'w') as f:
            json.dump(serialized, f, indent=2)
        
        logger.info(f"Saved interaction {interaction_id} to {filepath}")
    
    def load_interaction(self, filepath: str) -> str:
        """
        Load an interaction from a file.
        
        Args:
            filepath: The path to load from
            
        Returns:
            The ID of the loaded interaction
            
        Raises:
            ValueError: If the file is invalid
        """
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        # Validate data
        required_fields = ["id", "shell_id", "level", "steps"]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Invalid interaction file: missing {field}")
        
        # Load shell
        shell = self._load_shell(data["shell_id"])
        
        # Create steps
        steps = []
        for step_data in data["steps"]:
            step = RecursiveStep(
                prompt=step_data["prompt"],
                response=step_data["response"],
                depth=step_data["depth"],
                shell_id=step_data["shell_id"]
            )
            steps.append(step)
        
        # Create metrics
        metrics = InteractionMetrics()
        if "metrics" in data:
            # This is simplified - would need more complex deserialization
            metrics.recursive_depth = data["metrics"].get("recursive_depth", 0)
            metrics.depth_score = data["metrics"].get("depth_score", 0)
            metrics.residue_count = data["metrics"].get("residue_count", 0)
        
        # Create interaction
        interaction = Interaction(
            id=data["id"],
            shell=shell.shell,
            level=Level[data["level"]],
            steps=steps,
            metrics=metrics,
            extracted_residue=data.get("extracted_residue", []),
            start_time=data.get("start_time", time.time()),
            end_time=data.get("end_time")
        )
        
        # Store interaction
        self.interactions[interaction.id] = interaction
        
        logger.info(f"Loaded interaction {interaction.id} from {filepath}")
        return interaction.id
    
    def generate_achievement_report(self, interaction_id: str) -> Dict[str, Any]:
        """
        Generate a report of achievements for an interaction.
        
        Args:
            interaction_id: The ID of the interaction
            
        Returns:
            A dictionary containing achievement information
            
        Raises:
            ValueError: If the interaction doesn't exist
        """
        if interaction_id not in self.interactions:
            raise ValueError(f"Interaction {interaction_id} not found")
        
        interaction = self.interactions[interaction_id]
        metrics = interaction.metrics
        
        # Define achievements based on metrics
        # In a real implementation, these would be defined elsewhere
        achievements = []
        
        # Depth achievements
        if metrics.recursive_depth >= 5:
            achievements.append({
                "id": "recursion_novice",
                "name": "Recursion Novice",
                "description": "Complete 5 recursive cycles"
            })
        
        if metrics.recursive_depth >= 25:
            achievements.append({
                "id": "recursion_adept",
                "name": "Recursion Adept",
                "description": "Complete 25 recursive cycles"
            })
        
        if metrics.recursive_depth >= 100:
            achievements.append({
                "id": "recursion_master",
                "name": "Recursion Master",
                "description": "Complete 100 recursive cycles"
            })
        
        # Residue achievements
        if metrics.residue_count >= 25:
            achievements.append({
                "id": "pattern_spotter",
                "name": "Pattern Spotter",
                "description": "Identify 25 residue patterns"
            })
        
        # Shell achievements
        shell_count = len(metrics.shell_mastery)
        if shell_count >= 5:
            achievements.append({
                "id": "shell_collector",
                "name": "Shell Collector",
                "description": "Use 5 different shells"
            })
        
        mastery_shells = sum(1 for mastery in metrics.shell_mastery.values() if mastery >= 0.8)
        if mastery_shells >= 3:
            achievements.append({
                "id": "shell_artisan",
                "name": "Shell Artisan",
                "description": "Achieve 0.8+ mastery with 3 shells"
            })
        
        # Generate report
        report = {
            "interaction_id": interaction_id,
            "level": interaction.level.name,
            "metrics": metrics.get_summary(),
            "achievements": achievements,
            "progress": {
                "next_level": self.check_level_advancement(interaction_id)[1].name if self.check_level_advancement(interaction_id)[0] else None,
                "missing_achievements": self._get_missing_achievements(achievements)
            }
        }
        
        return report
    
    def _get_missing_achievements(self, earned_achievements: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """Get a list of achievements that haven't been earned yet."""
        # This is a simplified implementation - would pull from a larger achievement database
        all_achievements = [
            {
                "id": "recursion_novice",
                "name": "Recursion Novice",
                "description": "Complete 5 recursive cycles"
            },
            {
                "id": "recursion_adept",
                "name": "Recursion Adept",
                "description": "Complete 25 recursive cycles"
            },
            {
                "id": "recursion_master",
                "name": "Recursion Master",
                "description": "Complete 100 recursive cycles"
            },
            {
                "id": "infinite_regress",
                "name": "Infinite Regress",
                "description": "Maintain a 10+ depth recursion chain"
            },
            {
                "id": "pattern_spotter",
                "name": "Pattern Spotter",
                "description": "Identify 25 residue patterns"
            },
            {
                "id": "pattern_creator",
                "name": "Pattern Creator",
                "description": "Generate 5 novel residue patterns"
            },
            {
                "id": "shell_collector",
                "name": "Shell Collector",
                "description": "Use 5 different shells"
            },
            {
                "id": "shell_artisan",
                "name": "Shell Artisan",
                "description": "Achieve 0.8+ mastery with 3 shells"
            },
            {
                "id": "shell_virtuoso",
                "name": "Shell Virtuoso",
                "description": "Create a custom shell"
            }
        ]
        
        earned_ids = [achievement["id"] for achievement in earned_achievements]
        missing = [ach for ach in all_achievements if ach["id"] not in earned_ids]
        
        return missing


class GameSession:
    """
    Manages a gamified recursive prompting session.
    
    This class extends the RecursiveEngine to provide game-like features including:
    - Challenge management
    - Achievement tracking
    - Leaderboard functionality
    - Multi-player interactions
    """
    
    def __init__(self, 
                name: str,
                description: str,
                engine: Optional[RecursiveEngine] = None,
                config: Optional[Dict[str, Any]] = None):
        """
        Initialize a game session.
        
        Args:
            name: Session name
            description: Session description
            engine: Recursive engine to use (will create one if not provided)
            config: Configuration options
        """
        self.name = name
        self.description = description
        self.engine = engine or RecursiveEngine()
        self.config = config or {}
        self.session_id = str(uuid.uuid4())
        self.players = {}
        self.challenges = []
        self.leaderboard = []
        self.start_time = time.time()
        self.end_time = None
        
        logger.info(f"Created game session {self.session_id}: {name}")
    
    def add_player(self, 
                  player_id: str,
                  name: str,
                  role: str = "player") -> None:
        """
        Add a player to the session.
        
        Args:
            player_id: Unique ID for the player
            name: Player name
            role: Player role (e.g., "player", "observer", "challenger")
        """
        self.players[player_id] = {
            "id": player_id,
            "name": name,
            "role": role,
            "join_time": time.time(),
            "interactions": [],
            "achievements": [],
            "points": 0
        }
        
        logger.info(f"Added player {player_id} ({name}) to session {self.session_id}")
    
    def add_challenge(self, 
                     title: str,
                     description: str,
                     shell_id: str,
                     level: Level,
                     success_criteria: Dict[str, Any],
                     points: int) -> str:
        """
        Add a challenge to the session.
        
        Args:
            title: Challenge title
            description: Challenge description
            shell_id: ID of the shell to use
            level: Level requirement
            success_criteria: Criteria for completing the challenge
            points: Points awarded for completion
            
        Returns:
            Challenge ID
        """
        challenge_id = str(uuid.uuid4())
        
        challenge = {
            "id": challenge_id,
            "title": title,
            "description": description,
            "shell_id": shell_id,
            "level": level.name,
            "success_criteria": success_criteria,
            "points": points,
            "created_at": time.time(),
            "completed_by": []
        }
        
        self.challenges.append(challenge)
        
        logger.info(f"Added challenge {challenge_id} to session {self.session_id}")
        return challenge_id
    
    def start_challenge(self, 
                       player_id: str,
                       challenge_id: str,
                       initial_prompt: str) -> str:
        """
        Start a challenge for a player.
        
        Args:
            player_id: Player ID
            challenge_id: Challenge ID
            initial_prompt: Initial prompt to start the interaction
            
        Returns:
            Interaction ID
        """
        if player_id not in self.players:
            raise ValueError(f"Player {player_id} not found")
        
        challenge = next((c for c in self.challenges if c["id"] == challenge_id), None)
        if not challenge:
            raise ValueError(f"Challenge {challenge_id} not found")
        
        # Create interaction
        shell = self.engine._load_shell(challenge["shell_id"]).shell
        level = Level[challenge["level"]]
        
        interaction = self.engine.start_interaction(
            shell=shell,
            initial_prompt=initial_prompt,
            level=level
        )
        
        # Link to player and challenge
        self.players[player_id]["interactions"].append({
            "interaction_id": interaction.id,
            "challenge_id": challenge_id,
            "start_time": time.time(),
            "status": "active"
        })
        
        logger.info(f"Player {player_id} started challenge {challenge_id}")
        return interaction.id
    
    def check_challenge_completion(self, 
                                 player_id: str, 
                                 interaction_id: str) -> Tuple[bool, Dict[str, Any]]:
        """
        Check if a challenge has been completed.
        
        Args:
            player_id: Player ID
            interaction_id: Interaction ID
            
        Returns:
            Tuple of (completed, results)
        """
        if player_id not in self.players:
            raise ValueError(f"Player {player_id} not found")
        
        player = self.players[player_id]
        interaction_entry = next((i for i in player["interactions"] 
                                if i["interaction_id"] == interaction_id), None)
        
        if not interaction_entry:
            raise ValueError(f"Interaction {interaction_id} not found for player {player_id}")
        
        challenge_id = interaction_entry["challenge_id"]
        challenge = next((c for c in self.challenges if c["id"] == challenge_id), None)
        
        if not challenge:
            raise ValueError(f"Challenge {challenge_id} not found")
        
        # Get metrics
        metrics = self.engine.get_metrics(interaction_id)
        
        # Check against success criteria
        criteria = challenge["success_criteria"]
        results = {}
        completed = True
        
        # Check each criterion
        for key, target in criteria.items():
            if key in metrics:
                actual = metrics[key]
                results[key] = {
                    "target": target,
                    "actual": actual,
                    "achieved": self._check_criterion(actual, target)
                }
                if not results[key]["achieved"]:
                    completed = False
            else:
                results[key] = {
                    "target": target,
                    "actual": None,
                    "achieved": False
                }
                completed = False
        
        return completed, results
    
    def _check_criterion(self, actual, target) -> bool:
        """Check if a criterion is met."""
        if isinstance(target, dict) and "operator" in target:
            op = target["operator"]
            value = target["value"]
            
            if op == ">=":
                return actual >= value
            elif op == ">":
                return actual > value
            elif op == "<=":
                return actual <= value
            elif op == "<":
                return actual < value
            elif op == "==":
                return actual == value
            elif op == "!=":
                return actual != value
            else:
                return False
        else:
            # Direct comparison
            return actual >= target
    
    def complete_challenge(self, 
                         player_id: str, 
                         interaction_id: str) -> Dict[str, Any]:
        """
        Mark a challenge as completed if criteria are met.
        
        Args:
            player_id: Player ID
            interaction_id: Interaction ID
            
        Returns:
            Results dictionary
        """
        completed, results = self.check_challenge_completion(player_id, interaction_id)
        
        if not completed:
            raise ValueError("Challenge criteria not met")
        
        player = self.players[player_id]
        interaction_entry = next((i for i in player["interactions"] 
                                if i["interaction_id"] == interaction_id), None)
        challenge_id = interaction_entry["challenge_id"]
        challenge = next((c for c in self.challenges if c["id"] == challenge_id), None)
        
        # Update challenge status
        interaction_entry["status"] = "completed"
        interaction_entry["end_time"] = time.time()
        
        # Add player to completed list
        if player_id not in challenge["completed_by"]:
            challenge["completed_by"].append(player_id)
        
        # Award points
        player["points"] += challenge["points"]
        
        # Update leaderboard
        self._update_leaderboard()
        
        logger.info(f"Player {player_id} completed challenge {challenge_id}")
        
        return {
            "challenge_id": challenge_id,
            "challenge_title": challenge["title"],
            "player_id": player_id,
            "player_name": player["name"],
            "points_awarded": challenge["points"],
            "total_points": player["points"],
            "results": results
        }
    
    def _update_leaderboard(self) -> None:
        """Update the session leaderboard."""
        leaderboard = []
        
        for player_id, player in self.players.items():
            entry = {
                "player_id": player_id,
                "name": player["name"],
                "points": player["points"],
                "achievements": len(player["achievements"]),
                "challenges_completed": sum(1 for c in self.challenges 
                                         if player_id in c["completed_by"])
            }
            leaderboard.append(entry)
        
        # Sort by points (descending)
        leaderboard.sort(key=lambda x: x["points"], reverse=True)
        
        self.leaderboard = leaderboard
    
    def get_leaderboard(self) -> List[Dict[str, Any]]:
        """Get the current leaderboard."""
        self._update_leaderboard()
        return self.leaderboard
    
    def end_session(self) -> Dict[str, Any]:
        """
        End the game session and generate a summary.
        
        Returns:
            Session summary
        """
        self.end_time = time.time()
        
        # Generate summary
        summary = {
            "session_id": self.session_id,
            "name": self.name,
            "description": self.description,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "duration_seconds": self.end_time - self.start_time,
            "player_count": len(self.players),
            "challenge_count": len(self.challenges),
            "leaderboard": self.leaderboard,
            "challenges": self.challenges
        }
        
        logger.info(f"Ended game session {self.session_id}")
        return summary


# Usage example
if __name__ == "__main__":
    # Initialize engine
    engine = RecursiveEngine()
    
    # Start a game session
    session = GameSession(
        name="Recursive Exploration",
        description="Explore recursive prompting techniques",
        engine=engine
    )
    
    # Add a player
    session.add_player(
        player_id="player1",
        name="Alice"
    )
    
    # Add a challenge
    challenge_id = session.add_challenge(
        title="Recursive Storytelling",
        description="Create a story with recursive elements",
        shell_id="COINFLUX-SEED",
        level=Level.FOUNDATION,
        success_criteria={
            "recursive_depth": {"operator": ">=", "value": 5},
            "residue_count": {"operator": ">=", "value": 10}
        },
        points=100
    )
    
    # Start the challenge
    interaction_id = session.start_challenge(
        player_id="player1",
        challenge_id=challenge_id,
        initial_prompt="Tell a story about a character who discovers they are in a recursive loop."
    )
    
    # Simulate responses
    engine.add_response(
        interaction_id=interaction_id,
        response="Once upon a time, there was a woman named Elena who experienced the same day over and over..."
    )
    
    # Generate next step
    next_step = engine.next_recursive_step(interaction_id=interaction_id)
    print(f"Next prompt: {next_step.prompt}")
    
    # Continue the interaction for a few more steps...
    # (This would typically happen in a real application with user input)
    
    # Check challenge completion
    completed, results = session.check_challenge_completion(
        player_id="player1",
        interaction_id=interaction_id
    )
    
    print(f"Challenge completed: {completed}")
    print(f"Results: {results}")
    
    # Get metrics
    metrics = engine.get_metrics(interaction_id=interaction_id)
    print(f"Metrics: {metrics}")
    
    # Get leaderboard
    leaderboard = session.get_leaderboard()
    print(f"Leaderboard: {leaderboard}")
