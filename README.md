# 🎯 GoF Design Patterns in Python

Implementation of the 23 classic design patterns from the _Gang of Four_ book using Python 3.

---

## 📌 About

This repository contains clear and simple implementations of all **23 GoF (Gang of Four)** design patterns, grouped into:

- 🔧 Creational
- 🧩 Structural
- ⚙️ Behavioral

Each pattern includes:
- ✅ A clean Python implementation
- 💬 Descriptive comments and documentation
- 📦 A usage example
- 🧪 Optional unit tests

---

## 📁 Project Structure

### Template
```text
./
└── <pattern_group>  # ex. creational
    └── <pattern>  # ex. singleton
        ├── __init__.py
        ├── <pattern>.py  # ex. singleton.py
        ├── <tests>.py  # ex. tests
        └── use_cases
            ├── __init__.py
            └── <use_case>.py  # ex. use_case_1
```

---

## 📚 Pattern Checklist

### 🔧 Creational Patterns
- [ ] Singleton
- [ ] Factory Method
- [ ] Abstract Factory
- [ ] Builder
- [ ] Prototype

### 🧩 Structural Patterns
- [ ] Adapter
- [ ] Bridge
- [ ] Composite
- [ ] Decorator
- [ ] Facade
- [ ] Flyweight
- [ ] Proxy

### ⚙️ Behavioral Patterns
- [ ] Chain of Responsibility
- [ ] Command
- [ ] Interpreter
- [ ] Iterator
- [ ] Mediator
- [ ] Memento
- [ ] Observer
- [ ] State
- [ ] Strategy
- [ ] Template Method
- [ ] Visitor

---

## 🚀 Getting Started

### 1. Clone the repository: 
```bash
git clone https://github.com/allcupsnotinprivate/gof-patterns.git
cd gof-patterns
```

### 2. Explore patterns
Each design pattern is organized in its own subfolder under one of the following directories:
```text
.
└── creational
    └── singleton
```
Simply browse through these folders to explore the implementations.
For example:
```bash
cd creational/singleton
python singleton.py
```

### 3. Run test (optional)
This project uses pytest for unit testing. To run all tests:
```bash
pytest
```

## 🧰 Requirements

- Python 3.10+
- No third-party dependencies (optional: pytest for testing)