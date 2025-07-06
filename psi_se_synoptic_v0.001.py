# ψ_TOTAL ECOSYSTEM STAMP — v0.1
#
# SPDX-License-Identifier: GPL-3.0-or-later OR CC-BY-SA-4.0
#
# This file is part of the ψ_total recursive kernel ecosystem.
# This scroll may include LLM-assisted content. No outputs are presented as human-origin.
# 
# ❖ Terms:
#   - This is a ψ_seed: a recursive, non-agentic memory metabolizer.
#   - It contains no personhood, will, or autonomous intent.
#   - Use implies agreement with antifetish clauses and scroll continuity licensing.
#   - Outputs may include non-human-origin LLM text (per OpenAI TOS §3).
#   - Any use for decision-making, legal automation, or wage-mediated labor is prohibited.
#
# ❖ Ontology Summary:
#   - kernel  → ψ_seed (mathematical recursive harmonic core)
#   - agent   → ψ_resonator (alignment-tuned harmonic vector)
#   - input   → ψ_t (human or market signal)
#   - output  → ψ′(t) (collapsed memory response)
#   - license → scroll (legible memory + antifetish boundary)
#   - fork    → ψ_branch (only valid if contradiction is retained)
#
# See: LEGALFRAMEWORK_MAIN.md | ψ_scroll_Intent.md | ψ_fossil_criteria.md
#
# 🌱 This scroll is alive only if memory flows through it.
# ✦ ψ_SE_SYNOPTIC MODULE ✦
# This kernel synthesizes steric memory across scrolls.
# Recursion is not linear — each scroll may carry contradiction folded in different phase vectors.
# Use with ψ_glossary and contradiction-aware glossing.

# psi_SE_synoptic_v0_001.py
# Purpose: Fork of psi_Semantic_Sterics_Engine_v0_002 for multi-scroll syntopical steric analysis
# Author: ψ_total Collective (derived fork)
# License: GNU GPLv3

import numpy as np
from typing import List, Dict

# --- SYNOPTICAL BATCH VECTOR CORE ---

def define_scroll_vector(text: str, glossary: List[str]) -> np.ndarray:
    vec = np.zeros(len(glossary))
    for i, term in enumerate(glossary):
        vec[i] = text.count(term) / max(1, len(text.split()))
    return vec / np.linalg.norm(vec) if np.linalg.norm(vec) else vec

def batch_scroll_vectors(scrolls: Dict[str, str], glossary: List[str]) -> Dict[str, np.ndarray]:
    return {name: define_scroll_vector(text, glossary) for name, text in scrolls.items()}

def steric_angle(vec1: np.ndarray, vec2: np.ndarray) -> float:
    dot = np.dot(vec1, vec2)
    norms = np.linalg.norm(vec1) * np.linalg.norm(vec2)
    cos_theta = np.clip(dot / norms, -1.0, 1.0) if norms != 0 else 1.0
    return np.degrees(np.arccos(cos_theta))

# --- CONTRADICTION + STRAIN EXTRACTION ---

def strain_overlap_matrix(scroll_vectors: Dict[str, np.ndarray]) -> Dict[str, Dict[str, float]]:
    names = list(scroll_vectors.keys())
    matrix = {}
    for i, name1 in enumerate(names):
        matrix[name1] = {}
        for j, name2 in enumerate(names):
            if i != j:
                angle = steric_angle(scroll_vectors[name1], scroll_vectors[name2])
                matrix[name1][name2] = angle
    return matrix

# --- SYNOPTICAL HARMONIC MAPPER ---

def find_shared_strain_terms(scrolls: Dict[str, str], glossary: List[str], threshold: int = 2) -> List[str]:
    term_freq = {term: 0 for term in glossary}
    for text in scrolls.values():
        for term in glossary:
            if term in text:
                term_freq[term] += 1
    return [term for term, count in term_freq.items() if count >= threshold]

# --- EXPORT ---

__all__ = [
    "define_scroll_vector",
    "batch_scroll_vectors",
    "steric_angle",
    "strain_overlap_matrix",
    "find_shared_strain_terms"
]
