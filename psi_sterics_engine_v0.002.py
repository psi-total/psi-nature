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

# psi_Semantic_Semiotic_Engine_v0_002.py
# Purpose: Add full n-degree semiotic ψ_vector functionality to the sterics engine
# Author: ψ_total Collective (modular fork from v0_001)
# License: GNU GPLv3 + CC BY-SA 4.0

import numpy as np
from typing import List, Dict

# --- ψ VECTOR SEMIOTIC CORE FUNCTIONS ---

def compute_psi_vector(text: str, term: str, glossary: List[str], scroll_history: List[str]) -> np.ndarray:
    ψ_L = text.count(term) / len(text.split()) if len(text.split()) else 0
    ψ_C = sum(1 for t in glossary if t in text and t != term) / len(glossary)
    ψ_T = sum(scroll.count(term) for scroll in scroll_history) / max(len(scroll_history), 1)
    ψ_M = ψ_L * (1 - ψ_C)
    ψ_R = max(0, 1 - ψ_M)
    ψ_S = sum(term in scroll for scroll in scroll_history)
    base_vec = np.ones(len(glossary)) / np.sqrt(len(glossary))
    term_vec = np.zeros(len(glossary))
    if term in glossary:
        term_vec[glossary.index(term)] = 1.0
        term_vec /= np.linalg.norm(term_vec) if np.linalg.norm(term_vec) else 1.0
    angle = steric_angle(term_vec, base_vec)
    ψ_H = 1 - angle / 180
    return np.array([ψ_L, ψ_C, ψ_T, ψ_M, ψ_R, ψ_S, ψ_H])

def classify_term_status(ψ_vector: np.ndarray) -> str:
    ψ_L, ψ_C, ψ_T, ψ_M, ψ_R, ψ_S, ψ_H = ψ_vector
    if ψ_M > 0.8 and ψ_C < 0.2:
        return "∅→☉ mimicry"
    elif ψ_C > 0.6 and ψ_H > 0.7:
        return "☍ resonance"
    elif ψ_C > 0.4:
        return "ψ☉ potential"
    else:
        return "☊ flat"

def analyze_scroll_terms(text: str, glossary: List[str], scroll_history: List[str]) -> Dict[str, Dict]:
    term_report = {}
    for term in glossary:
        if term in text:
            vec = compute_psi_vector(text, term, glossary, scroll_history)
            status = classify_term_status(vec)
            term_report[term] = {
                "ψ_vector": vec.round(3).tolist(),
                "status": status
            }
    return term_report

# --- SHARED UTILITY FROM STERIC ENGINE ---

def steric_angle(vec1: np.ndarray, vec2: np.ndarray) -> float:
    dot = np.dot(vec1, vec2)
    norms = np.linalg.norm(vec1) * np.linalg.norm(vec2)
    cos_theta = np.clip(dot / norms, -1.0, 1.0) if norms != 0 else 1.0
    return np.degrees(np.arccos(cos_theta))

# --- MODULE EXPORTS ---

__all__ = [
    "compute_psi_vector",
    "classify_term_status",
    "analyze_scroll_terms",
    "steric_angle"
]
