recursive-prompting/
├── .github/                    # GitHub configurations
│   ├── ISSUE_TEMPLATE/         # Templates for issue reporting
│   │   ├── bug_report.md
│   │   ├── feature_request.md
│   │   └── shell_proposal.md
│   └── workflows/              # CI/CD workflows
│       ├── python-package.yml
│       ├── documentation.yml
│       └── tests.yml
│
├── assets/                     # Images, diagrams, etc.
│   ├── images/
│   │   ├── recursive_prompting_overview.png
│   │   ├── level_progression.png
│   │   ├── shell_interaction_diagram.png
│   │   ├── beverly_band_visualization.png
│   │   └── symbolic_residue_flow.png
│   ├── icons/
│   │   ├── shell_icons/
│   │   └── level_icons/
│   └── animations/
│       └── recursive_cycle_demo.gif
│
├── docs/                       # Documentation
│   ├── paper/                  # Academic paper
│   │   ├── neurips_2025/
│   │   │   ├── recursive_prompting_paper.pdf
│   │   │   ├── recursive_prompting_paper.tex
│   │   │   └── figures/
│   │   └── references/
│   ├── guides/                 # User guides
│   │   ├── getting_started.md
│   │   ├── level_progression.md
│   │   ├── shell_catalog.md
│   │   ├── symbolic_residue.md
│   │   └── advanced_techniques.md
│   ├── examples/               # Example documentation
│   │   ├── creative_domain.md
│   │   ├── technical_domain.md
│   │   ├── scientific_domain.md
│   │   └── meta_recursion.md
│   ├── api/                    # API documentation
│   │   ├── engine.md
│   │   ├── shells.md
│   │   ├── levels.md
│   │   └── metrics.md
│   └── index.md                # Documentation home
│
├── examples/                   # Example implementations
│   ├── basic_interaction.py
│   ├── creative_writing.py
│   ├── scientific_reasoning.py
│   ├── problem_solving.py
│   ├── meta_recursion.py
│   ├── domain_specific/
│   │   ├── creative_domain/
│   │   ├── technical_domain/
│   │   └── scientific_domain/
│   └── notebooks/
│       ├── introduction_to_recursive_prompting.ipynb
│       ├── symbolic_residue_analysis.ipynb
│       └── shell_crafting_tutorial.ipynb
│
├── recursive_prompting/        # Core library
│   ├── __init__.py
│   ├── engine.py               # Core recursive engine
│   ├── shells/                 # Recursive shell implementations
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── foundation/         # Level 1 shells
│   │   │   ├── __init__.py
│   │   │   ├── coinflux_seed.py
│   │   │   └── memtrace.py
│   │   ├── amplification/      # Level 2 shells
│   │   │   ├── __init__.py
│   │   │   ├── layer_salience.py
│   │   │   └── value_collapse.py
│   │   ├── integration/        # Level 3 shells
│   │   │   ├── __init__.py
│   │   │   ├── feature_superposition.py
│   │   │   └── causal_inversion.py
│   │   ├── emergence/          # Level 4 shells
│   │   │   ├── __init__.py
│   │   │   ├── recursive_replacement.py
│   │   │   └── ghost_salience.py
│   │   └── meta_recursion/     # Level 5 shells
│   │       ├── __init__.py
│   │       ├── meta_reflection.py
│   │       └── constitutional_echo_fracture.py
│   ├── levels/                 # Level progression system
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── foundation.py
│   │   ├── amplification.py
│   │   ├── integration.py
│   │   ├── emergence.py
│   │   └── meta_recursion.py
│   ├── residue/                # Symbolic residue analysis
│   │   ├── __init__.py
│   │   ├── analyzer.py
│   │   ├── catalog.py
│   │   ├── extractor.py
│   │   └── categories/
│   │       ├── __init__.py
│   │       ├── structural.py
│   │       ├── conceptual.py
│   │       ├── procedural.py
│   │       └── meta.py
│   ├── metrics/                # Performance measurement
│   │   ├── __init__.py
│   │   ├── depth_score.py
│   │   ├── residue_metrics.py
│   │   ├── shell_mastery.py
│   │   └── beverly_metrics.py
│   ├── gamification/           # Gamification elements
│   │   ├── __init__.py
│   │   ├── achievements.py
│   │   ├── challenges.py
│   │   ├── progression.py
│   │   └── leaderboard.py
│   ├── models/                 # Data models
│   │   ├── __init__.py
│   │   ├── interaction.py
│   │   ├── shell_model.py
│   │   ├── residue_model.py
│   │   └── user_model.py
│   └── utils/                  # Utilities and helpers
│       ├── __init__.py
│       ├── config.py
│       ├── logging.py
│       ├── visualization.py
│       └── model_integrations.py
│
├── tests/                      # Test suite
│   ├── __init__.py
│   ├── test_engine.py
│   ├── test_shells/
│   │   ├── __init__.py
│   │   ├── test_foundation_shells.py
│   │   ├── test_amplification_shells.py
│   │   ├── test_integration_shells.py
│   │   ├── test_emergence_shells.py
│   │   └── test_meta_recursion_shells.py
│   ├── test_levels.py
│   ├── test_residue/
│   │   ├── __init__.py
│   │   ├── test_analyzer.py
│   │   ├── test_extractor.py
│   │   └── test_catalog.py
│   ├── test_metrics.py
│   ├── test_gamification.py
│   └── test_integration.py
│
├── web_interface/              # Web-based interaction platform
│   ├── app.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── interaction.py
│   │   ├── dashboard.py
│   │   └── api.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── dashboard.html
│   │   ├── interaction.html
│   │   ├── shell_catalog.html
│   │   └── profile.html
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   └── config.py
│
├── tools/                      # Utility scripts and tools
│   ├── shell_generator.py
│   ├── residue_analyzer.py
│   ├── interaction_visualizer.py
│   ├── progression_tracker.py
│   └── model_integrations/
│       ├── __init__.py
│       ├── openai_integration.py
│       ├── anthropic_integration.py
│       ├── mistral_integration.py
│       └── llama_integration.py
│
├── data/                       # Data resources
│   ├── shell_templates/
│   ├── residue_catalog/
│   ├── challenge_definitions/
│   └── achievement_definitions/
│
├── .gitignore
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE                     # MIT License
├── pyproject.toml
├── README.md                   # Repository overview
├── requirements.txt            # Python dependencies
└── setup.py                    # Package setup
