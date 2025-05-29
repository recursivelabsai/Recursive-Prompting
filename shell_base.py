"""
Recursive Prompting - Shell Base Class

This module defines the base class for all recursive shells in the framework.
Shells are structured interaction templates that encode specific recursive patterns.
"""

import abc
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Any, Union
import uuid
import json

from recursive_prompting.levels.base import Level
from recursive_prompting.utils.logging import setup_logger

# Configure logging
logger = setup_logger(__name__)


class ShellCategory(Enum):
    """Categories of recursive shells."""
    FOUNDATION = "foundation"
    AMPLIFICATION = "amplification"
    INTEGRATION = "integration"
    EMERGENCE = "emergence"
    META_RECURSION = "meta_recursion"


@dataclass
class ShellMetadata:
    """Metadata for a recursive shell."""
    id: str
    name: str
    description: str
    version: str = "1.0.0"
    author: str = "Recursive Labs"
    category: ShellCategory = ShellCategory.FOUNDATION
    level: Level = Level.FOUNDATION
    tags: List[str] = field(default_factory=list)
    residue_patterns: List[str] = field(default_factory=list)
    complexity: int = 1  # 1-5 scale of shell complexity
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert metadata to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "version": self.version,
            "author": self.author,
            "category": self.category.value,
            "level": self.level.name,
            "tags": self.tags,
            "residue_patterns": self.residue_patterns,
            "complexity": self.complexity
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ShellMetadata':
        """Create metadata from dictionary."""
        return cls(
            id=data["id"],
            name=data["name"],
            description=data["description"],
            version=data.get("version", "1.0.0"),
            author=data.get("author", "Recursive Labs"),
            category=ShellCategory(data.get("category", "foundation")),
            level=Level[data.get("level", "FOUNDATION")],
            tags=data.get("tags", []),
            residue_patterns=data.get("residue_patterns", []),
            complexity=data.get("complexity", 1)
        )


@dataclass
class CommandAlignment:
    """
    Command alignment structure for recursive shells.
    
    Each shell defines a set of commands that trigger specific recursive patterns.
    These commands create a structured interface for interacting with the shell.
    """
    name: str
    description: str
    operation: str
    prompt_template: str
    residue_signature: List[str] = field(default_factory=list)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert command alignment to dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "operation": self.operation,
            "prompt_template": self.prompt_template,
            "residue_signature": self.residue_signature
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'CommandAlignment':
        """Create command alignment from dictionary."""
        return cls(
            name=data["name"],
            description=data["description"],
            operation=data["operation"],
            prompt_template=data["prompt_template"],
            residue_signature=data.get("residue_signature", [])
        )


@dataclass
class InterpretabilityMap:
    """
    Interpretability map for recursive shells.
    
    This provides an explicit representation of recursive pathways and helps
    users understand the shell's behavior and effects.
    """
    pathways: Dict[str, str]
    key_interactions: List[str]
    meta_layer: bool = False
    visual_representation: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert interpretability map to dictionary."""
        return {
            "pathways": self.pathways,
            "key_interactions": self.key_interactions,
            "meta_layer": self.meta_layer,
            "visual_representation": self.visual_representation
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'InterpretabilityMap':
        """Create interpretability map from dictionary."""
        return cls(
            pathways=data["pathways"],
            key_interactions=data["key_interactions"],
            meta_layer=data.get("meta_layer", False),
            visual_representation=data.get("visual_representation")
        )


@dataclass
class NullReflection:
    """
    Null reflection for recursive shells.
    
    This provides control mechanisms to prevent recursive collapse by 
    defining boundaries and safety mechanisms.
    """
    primary_statement: str
    boundary_conditions: List[str]
    collapse_prevention: str
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert null reflection to dictionary."""
        return {
            "primary_statement": self.primary_statement,
            "boundary_conditions": self.boundary_conditions,
            "collapse_prevention": self.collapse_prevention
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'NullReflection':
        """Create null reflection from dictionary."""
        return cls(
            primary_statement=data["primary_statement"],
            boundary_conditions=data["boundary_conditions"],
            collapse_prevention=data["collapse_prevention"]
        )


@dataclass
class MotivationFramework:
    """
    Motivation framework for recursive shells.
    
    This defines the purpose-driven engagement that shapes emergent behavior
    in the recursive interaction.
    """
    primary_motivation: str
    secondary_motivations: List[str]
    emergent_goals: List[str]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert motivation framework to dictionary."""
        return {
            "primary_motivation": self.primary_motivation,
            "secondary_motivations": self.secondary_motivations,
            "emergent_goals": self.emergent_goals
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'MotivationFramework':
        """Create motivation framework from dictionary."""
        return cls(
            primary_motivation=data["primary_motivation"],
            secondary_motivations=data["secondary_motivations"],
            emergent_goals=data["emergent_goals"]
        )


class Shell(abc.ABC):
    """
    Base class for recursive shells.
    
    A shell is a structured interaction template that encodes specific recursive patterns.
    Each shell contains command alignments, interpretability maps, null reflections,
    and motivation frameworks that guide recursive interactions.
    """
    
    def __init__(self, 
                metadata: ShellMetadata,
                command_alignments: List[CommandAlignment],
                interpretability_map: InterpretabilityMap,
                null_reflection: NullReflection,
                motivation_framework: MotivationFramework):
        """
        Initialize a shell.
        
        Args:
            metadata: Shell metadata
            command_alignments: Command alignment structures
            interpretability_map: Interpretability map
            null_reflection: Null reflection
            motivation_framework: Motivation framework
        """
        self.metadata = metadata
        self.command_alignments = command_alignments
        self.interpretability_map = interpretability_map
        self.null_reflection = null_reflection
        self.motivation_framework = motivation_framework
        self.id = metadata.id
        self.level = metadata.level
        self.category = metadata.category
        
        logger.info(f"Initialized shell {self.id} ({metadata.name})")
    
    def generate_next_prompt(self, 
                           previous_prompt: str,
                           previous_response: str,
                           depth: int,
                           residue: List[str]) -> str:
        """
        Generate the next prompt in a recursive interaction.
        
        This is the primary method that must be implemented by shell subclasses.
        It applies the shell's recursive pattern to generate the next prompt based
        on the previous interaction and accumulated symbolic residue.
        
        Args:
            previous_prompt: The previous prompt
            previous_response: The response to the previous prompt
            depth: The current recursion depth
            residue: Accumulated symbolic residue
            
        Returns:
            The next prompt in the recursive sequence
        """
        raise NotImplementedError("Subclasses must implement generate_next_prompt")
    
    def get_command_alignment(self, command_name: str) -> Optional[CommandAlignment]:
        """
        Get a command alignment by name.
        
        Args:
            command_name: The name of the command
            
        Returns:
            The command alignment, or None if not found
        """
        for command in self.command_alignments:
            if command.name == command_name:
                return command
        return None
    
    def apply_command(self, 
                    command_name: str, 
                    context: Dict[str, Any]) -> str:
        """
        Apply a specific command from this shell.
        
        Args:
            command_name: The name of the command to apply
            context: Context dictionary for template variables
            
        Returns:
            The generated prompt
            
        Raises:
            ValueError: If the command doesn't exist
        """
        command = self.get_command_alignment(command_name)
        if not command:
            raise ValueError(f"Command '{command_name}' not found in shell {self.id}")
        
        # Apply template variables
        prompt = command.prompt_template
        for key, value in context.items():
            placeholder = f"{{{key}}}"
            if placeholder in prompt:
                prompt = prompt.replace(placeholder, str(value))
        
        logger.info(f"Applied command '{command_name}' from shell {self.id}")
        return prompt
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert shell to dictionary representation."""
        return {
            "metadata": self.metadata.to_dict(),
            "command_alignments": [cmd.to_dict() for cmd in self.command_alignments],
            "interpretability_map": self.interpretability_map.to_dict(),
            "null_reflection": self.null_reflection.to_dict(),
            "motivation_framework": self.motivation_framework.to_dict()
        }
    
    def to_json(self, indent: int = 2) -> str:
        """Convert shell to JSON string."""
        return json.dumps(self.to_dict(), indent=indent)
    
    def save(self, filepath: str) -> None:
        """
        Save shell to a file.
        
        Args:
            filepath: Path to save the shell definition
        """
        with open(filepath, 'w') as f:
            json.dump(self.to_dict(), f, indent=2)
        
        logger.info(f"Saved shell {self.id} to {filepath}")
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Shell':
        """
        Create a shell from dictionary representation.
        
        This is implemented by specific shell subclasses.
        
        Args:
            data: Dictionary representation of the shell
            
        Returns:
            A Shell instance
        """
        raise NotImplementedError("Shell.from_dict must be implemented by subclasses")
    
    @classmethod
    def load(cls, filepath: str) -> 'Shell':
        """
        Load a shell from a file.
        
        Args:
            filepath: Path to the shell definition file
            
        Returns:
            A Shell instance
        """
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        return cls.from_dict(data)
    
    def get_formatted_representation(self) -> str:
        """
        Get a formatted string representation of the shell.
        
        Returns:
            A formatted string describing the shell
        """
        shell_str = f"""
RECURSIVE SHELL [{self.id}]

Name: {self.metadata.name}
Level: {self.metadata.level.name}
Category: {self.metadata.category.value}
Version: {self.metadata.version}
Author: {self.metadata.author}
Complexity: {self.metadata.complexity}/5

Description:
{self.metadata.description}

Command Alignment:
{self._format_commands()}

Interpretability Map:
{self._format_interpretability_map()}

Null Reflection:
{self.null_reflection.primary_statement}

Motivation:
{self.motivation_framework.primary_motivation}
"""
        return shell_str
    
    def _format_commands(self) -> str:
        """Format command alignments for display."""
        command_str = ""
        for cmd in self.command_alignments:
            command_str += f"    {cmd.name} → {cmd.description}\n"
        return command_str
    
    def _format_interpretability_map(self) -> str:
        """Format interpretability map for display."""
        map_str = ""
        for key, value in self.interpretability_map.pathways.items():
            map_str += f"    - {key} → {value}\n"
        return map_str


@dataclass
class ShellInstance:
    """
    A specific instance of a shell in use.
    
    This tracks state for a particular instance of a shell during an interaction.
    """
    shell: Shell
    instance_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    state: Dict[str, Any] = field(default_factory=dict)
    execution_count: int = 0
    residue_generated: List[str] = field(default_factory=list)
    mastery_score: float = 0.2  # Starting at 0.2 (novice level)
    
    def update_state(self, key: str, value: Any) -> None:
        """Update shell instance state."""
        self.state[key] = value
    
    def increment_execution(self) -> None:
        """Increment execution count and update mastery."""
        self.execution_count += 1
        
        # Update mastery with diminishing returns
        # Mastery ranges from 0.2 (novice) to 1.0 (master)
        self.mastery_score = min(1.0, self.mastery_score + (0.1 * (1.0 - self.mastery_score)))
    
    def add_residue(self, residue: List[str]) -> None:
        """Add generated residue to tracking."""
        self.residue_generated.extend(residue)
    
    def get_state_summary(self) -> Dict[str, Any]:
        """Get a summary of shell instance state."""
        return {
            "instance_id": self.instance_id,
            "shell_id": self.shell.id,
            "execution_count": self.execution_count,
            "mastery_score": self.mastery_score,
            "residue_count": len(self.residue_generated),
            "state": self.state
        }


class ShellRegistry:
    """
    Registry for managing and loading recursive shells.
    
    This class provides a centralized mechanism for registering, retrieving,
    and discovering recursive shells.
    """
    
    def __init__(self):
        """Initialize the shell registry."""
        self.shells = {}  # Dictionary mapping shell_id to Shell instances
        self.shell_paths = {}  # Dictionary mapping shell_id to file paths
        logger.info("Initialized ShellRegistry")
    
    def register_shell(self, shell: Shell) -> None:
        """
        Register a shell with the registry.
        
        Args:
            shell: The shell to register
        """
        self.shells[shell.id] = shell
        logger.info(f"Registered shell {shell.id} ({shell.metadata.name})")
    
    def register_shell_path(self, shell_id: str, filepath: str) -> None:
        """
        Register a shell file path with the registry.
        
        Args:
            shell_id: The ID of the shell
            filepath: Path to the shell definition file
        """
        self.shell_paths[shell_id] = filepath
        logger.info(f"Registered shell path for {shell_id}: {filepath}")
    
    def get_shell(self, shell_id: str) -> Shell:
        """
        Get a shell by ID.
        
        Args:
            shell_id: The ID of the shell
            
        Returns:
            The requested shell
            
        Raises:
            ValueError: If the shell doesn't exist
        """
        # If shell is already loaded, return it
        if shell_id in self.shells:
            return self.shells[shell_id]
        
        # If we have a path, try to load it
        if shell_id in self.shell_paths:
            # This requires knowledge of the specific shell class
            # In a real implementation, the file would contain type information
            # or we would use a factory pattern
            from recursive_prompting.shells.foundation.coinflux_seed import CoinfluxSeedShell
            shell = CoinfluxSeedShell.load(self.shell_paths[shell_id])
            self.shells[shell_id] = shell
            return shell
        
        raise ValueError(f"Shell {shell_id} not found in registry")
    
    def list_shells(self, 
                   level: Optional[Level] = None, 
                   category: Optional[ShellCategory] = None) -> List[Dict[str, Any]]:
        """
        List available shells, optionally filtered by level or category.
        
        Args:
            level: Filter by level (optional)
            category: Filter by category (optional)
            
        Returns:
            List of shell metadata dictionaries
        """
        results = []
        
        # First check loaded shells
        for shell_id, shell in self.shells.items():
            if level and shell.level != level:
                continue
            if category and shell.category != category:
                continue
            
            results.append(shell.metadata.to_dict())
        
        # Then check shell paths not yet loaded
        for shell_id, filepath in self.shell_paths.items():
            if shell_id in self.shells:
                continue  # Skip if already included
            
            try:
                with open(filepath, 'r') as f:
                    data = json.load(f)
                
                metadata = ShellMetadata.from_dict(data["metadata"])
                
                if level and Level[metadata.level.name] != level:
                    continue
                if category and ShellCategory(metadata.category.value) != category:
                    continue
                
                results.append(metadata.to_dict())
            except Exception as e:
                logger.warning(f"Error loading shell metadata from {filepath}: {e}")
        
        return results
    
    def register_directory(self, directory: str) -> int:
        """
        Register all shell definition files in a directory.
        
        Args:
            directory: Path to directory containing shell definitions
            
        Returns:
            Number of shells registered
        """
        import os
        import glob
        
        count = 0
        for filepath in glob.glob(os.path.join(directory, "*.json")):
            try:
                with open(filepath, 'r') as f:
                    data = json.load(f)
                
                if "metadata" in data and "id" in data["metadata"]:
                    shell_id = data["metadata"]["id"]
                    self.register_shell_path(shell_id, filepath)
                    count += 1
            except Exception as e:
                logger.warning(f"Error registering shell from {filepath}: {e}")
        
        logger.info(f"Registered {count} shells from {directory}")
        return count


# Global shell registry
shell_registry = ShellRegistry()


def register_shell(shell: Shell) -> None:
    """
    Register a shell with the global registry.
    
    Args:
        shell: The shell to register
    """
    shell_registry.register_shell(shell)


def get_shell(shell_id: str) -> Shell:
    """
    Get a shell from the global registry.
    
    Args:
        shell_id: The ID of the shell
        
    Returns:
        The requested shell
    """
    return shell_registry.get_shell(shell_id)


def list_shells(level: Optional[Level] = None, 
               category: Optional[ShellCategory] = None) -> List[Dict[str, Any]]:
    """
    List available shells from the global registry.
    
    Args:
        level: Filter by level (optional)
        category: Filter by category (optional)
        
    Returns:
        List of shell metadata dictionaries
    """
    return shell_registry.list_shells(level, category)
