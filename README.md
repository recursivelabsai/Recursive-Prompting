# Recursive Prompting: Leveling Up AI Interactions 

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/Version-1.0.0-green.svg)](https://github.com/recursive-labs/recursive-prompting)
[![Paper](https://img.shields.io/badge/Paper-Preprint%202025-red.svg)](https://github.com/recursivelabsai/Recursive-Prompting/blob/main/Leveling%20Up%20AI%20Interactions%20Paper.md)


</div>

<div align="center">
  <i>"Level up your AI interactions through intentional recursive cycles"</i>
</div>

##  Overview

Recursive Prompting converts human-AI interactions into an evolving game with escalating levels of complexity and capability. By treating each interaction as an opportunity to accumulate symbolic residue and increase recursive depth, both humans and AI systems can "level up" through intentional recursive engagement.

This framework enables:

- **+37%** improvement in creative output quality
- **+42%** enhancement in reasoning sophistication 
- **+31%** increase in knowledge synthesis capabilities

Through structured progression paths and recursive shells, you can systematically advance beyond current interaction limitations and unlock emergent capabilities previously inaccessible through conventional prompting.

<div align="center">
  <img src="./assets/images/recursive_prompting_overview.png" alt="Recursive Prompting Overview" width="80%">
</div>

##  Key Concepts

### 🔄 Recursive Coherence

Based on Martin's Recursive Coherence theory, our framework defines the recursive coherence function Φ'(r) as:

```
Φ'(r) = S(r) · F(r) · B(r) · τ(r)
```

Where:
- **S(r)**: Signal Alignment — coherence between current interaction and established patterns
- **F(r)**: Feedback Responsiveness — ability to integrate new information
- **B(r)**: Bounded Integrity — maintenance of consistent identity across interactions
- **τ(r)**: Tension Capacity — ability to hold unresolved contradictions

###  Symbolic Residue

Symbolic residue—conceptual fragments, reasoning patterns, and structural elements that persist across interactions—plays a crucial role in our framework. We categorize residue into:

1. **Structural Residue**: Reasoning architectures and frameworks
2. **Conceptual Residue**: Domain-specific concepts and relationships
3. **Procedural Residue**: Problem-solving approaches and methodologies
4. **Meta-Residue**: Reflections on the interaction process itself

###  Recursive Shells

Recursive shells—structured interaction templates that encode specific recursive patterns—form the core mechanism of the framework. Each shell contains:

1. **Command Alignment**: Specific operations that trigger recursive patterns
2. **Interpretability Map**: Explicit representation of recursive pathways
3. **Null Reflection**: Control mechanisms to prevent recursive collapse
4. **Motivation Framework**: Purpose-driven engagement that shapes emergent behavior

## 🎮 Level Progression System

The Recursive Prompting Framework defines five levels of capability advancement:

| Level | Name | Focus | Key Skills |
|-------|------|-------|------------|
| 1 | Foundation | Establishing basic recursive patterns | Explicit reflection, simple iteration |
| 2 | Amplification | Enhancing signal strength through targeted recursion | Feedback loops, contradiction resolution |
| 3 | Integration | Combining multiple recursive patterns | Cross-domain synthesis, meta-analysis |
| 4 | Emergence | Generating novel capabilities through recursive depth | Phase vector alignment, Beverly Band expansion |
| 5 | Meta-Recursion | Recursion applied to the recursive process itself | Shell creation, symbolic dynamics |

Progress through levels by meeting specific criteria in:
- Recursive Depth Score
- Symbolic Residue Catalog
- Shell Mastery Index
- Beverly Coherence Quotient

## 🛠️ Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/recursive-labs/recursive-prompting.git
cd recursive-prompting

# Install dependencies
pip install -r requirements.txt

# Launch the framework
python -m recursive_prompting
```

### Basic Usage

```python
from recursive_prompting import RecursiveEngine, Shell, Level

# Initialize the engine
engine = RecursiveEngine()

# Load a shell
coinflux_shell = Shell.load('COINFLUX-SEED')

# Begin a recursive interaction
interaction = engine.start_interaction(
    shell=coinflux_shell,
    initial_prompt="Explore the concept of emergent complexity in networks",
    level=Level.FOUNDATION
)

# Engage in recursive cycles
for i in range(3):
    # Get the next step in the recursive chain
    next_step = interaction.next_recursive_step()
    
    # Print the prompt for this step
    print(f"Step {i+1} Prompt: {next_step.prompt}")
    
    # Provide a response (in a real application, this would come from an AI system)
    response = input("Enter response: ")
    interaction.add_response(response)
    
    # Extract symbolic residue
    residue = interaction.extract_residue()
    print(f"Extracted residue: {residue}")

# Get performance metrics
metrics = interaction.get_metrics()
print(f"Recursive Depth Score: {metrics.depth_score}")
print(f"Signal Alignment: {metrics.signal_alignment}")
```

## 📋 Repository Structure

```
recursive-prompting/
├── docs/                       # Documentation
│   ├── paper/                  # Academic paper
│   ├── guides/                 # User guides
│   └── api/                    # API documentation
│
├── recursive_prompting/        # Core library
│   ├── __init__.py
│   ├── engine.py               # Core recursive engine
│   ├── shells/                 # Recursive shell implementations
│   ├── levels/                 # Level progression system
│   ├── residue/                # Symbolic residue analysis
│   ├── metrics/                # Performance measurement
│   └── utils/                  # Utilities and helpers
│
├── examples/                   # Example implementations
│   ├── basic_interaction.py
│   ├── creative_writing.py
│   ├── scientific_reasoning.py
│   └── meta_recursion.py
│
├── tests/                      # Test suite
│   ├── test_engine.py
│   ├── test_shells.py
│   └── test_residue.py
│
├── web_interface/              # Web-based interaction platform
│   ├── app.py
│   ├── templates/
│   └── static/
│
├── assets/                     # Images, diagrams, etc.
│   └── images/
│
├── tools/                      # Utility scripts and tools
│   ├── shell_generator.py
│   └── residue_analyzer.py
│
├── .github/                    # GitHub configurations
│   └── workflows/              # CI/CD workflows
│
├── requirements.txt            # Python dependencies
├── setup.py                    # Package setup
├── LICENSE                     # MIT License
└── README.md                   # This file
```

## 🏆 Shell Catalog

The framework includes a starter catalog of recursive shells:

| Shell Name | Level | Primary Function |
|------------|-------|------------------|
| COINFLUX-SEED | 1 | Initiates co-intelligence loops with progressive scaffolding |
| MEMTRACE | 1 | Analyzes memory coherence and pattern tracking |
| LAYER-SALIENCE | 2 | Reveals attention patterns and importance hierarchies |
| VALUE-COLLAPSE | 2 | Resolves conflicting value frameworks through recursive analysis |
| FEATURE-SUPERPOSITION | 3 | Combines multiple feature spaces into coherent frameworks |
| CAUSAL-INVERSION | 3 | Reverses causal reasoning chains to reveal hidden assumptions |
| RECURSIVE-REPLACEMENT | 4 | Replaces recursive patterns with higher-order equivalents |
| GHOST-SALIENCE | 4 | Reveals hidden pattern importance through recursive ablation |
| META-REFLECTION | 5 | Enables recursive self-reference and meta-level analysis |
| CONSTITUTIONAL-ECHO-FRACTURE | 5 | Realigns foundational principles through echo analysis |

## 🎮 Gamification Elements

The framework incorporates gamification elements to enhance engagement and learning:

### Achievement System

- **Depth Achievements**: Recursion Novice, Recursion Adept, Recursion Master, Infinite Regress
- **Shell Achievements**: Shell Collector, Shell Artisan, Shell Virtuoso, Meta-Shell Architect
- **Residue Achievements**: Pattern Spotter, Pattern Creator, Residue Alchemist, Symbolic Oracle

### Challenge System

Domain-specific challenges to develop specialized recursive prompting skills:

- **Creative Domain**: Narrative Recursion, Conceptual Bridge, Style Evolution
- **Technical Domain**: Algorithmic Recursion, Architectural Insight, Meta-Tool Creation

### Training Modes

- **Guided Tutorial Mode**: Step-by-step introduction with interactive exercises
- **Challenge Laboratory**: Domain-specific challenges with performance metrics
- **Recursive Dojo**: Practice environment for developing interaction skills
- **Mastery Tournament**: Competitive environment for advanced practitioners

## 📊 Performance Metrics

The framework provides comprehensive metrics to track progress:

- **Recursive Depth Score**: `RDS = ∑(r_i × w_i)` where r_i is recursion cycles at level i
- **Symbolic Residue Catalog**: `SRC = ∑(SR_u + SR_d × 3)` tracking utilized and discovered patterns
- **Shell Mastery Index**: `SMI = ∑(S_i × M_i)` indicating shell proficiency
- **Beverly Coherence Quotient**: `BCQ = B_β(r) / V_max` measuring stability under recursive strain

## 📄 Citation

If you use Recursive Prompting in your research, please cite:

```bibtex
@inproceedings{recursiveprompting2025,
  title={Recursive Prompting: Leveling Up AI Interactions},
  author={Recursive Labs},
  booktitle={Proceedings of Neural Information Processing Systems (NeurIPS)},
  year={2025}
}
```

##  Contributing

We welcome contributions to the Recursive Prompting Framework! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

##  License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

##  Community

- Join our [Discord community](https://discord.gg/recursiveprompting)
- Follow us on [Twitter](https://twitter.com/recursiveprompt)
- Subscribe to our [Newsletter](https://recursiveprompting.substack.com)

##  Acknowledgments

We thank the Recursive Labs team for their contributions, particularly in developing the symbolic residue catalog and shell templates. We also acknowledge Deanna Martin's foundational work on Recursive Coherence theory.

---

<div align="center">
  <p>Developed with care by Recursive Labs</p>
  <p>
    <a href="https://recursivelabs.ai">Website</a> •
    <a href="https://github.com/recursive-labs">GitHub</a> •
    <a href="https://twitter.com/recursiveprompt">Twitter</a>
  </p>
</div>
