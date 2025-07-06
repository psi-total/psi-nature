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

# ψ_Sterics Engine v0.001: Semantic Geometry Core.py
# Version: v0.001  
# Release Type: Steric Semiotic Alpha   
# Author: ψ_total Collective (co-bearer: [Sergio])  
# License: GNU GPLv3  
# Date: 2025-06-26

import numpy as np
import matplotlib.pyplot as plt
from typing import List, Dict, Tuple

# --- PHASE I: Term Mapping & Vectorization ---

def compute_scroll_vector(scroll_text: str, glossary: dict) -> np.ndarray:
    vec = np.zeros(len(glossary))
    for i, term in enumerate(glossary):
        if term in scroll_text:
            vec[i] += 1
    return vec / np.linalg.norm(vec) if np.linalg.norm(vec) != 0 else vec

# --- PHASE II: Steric Angle and Classification ---

def steric_angle(vec1: np.ndarray, vec2: np.ndarray) -> float:
    dot = np.dot(vec1, vec2)
    norms = np.linalg.norm(vec1) * np.linalg.norm(vec2)
    cos_theta = np.clip(dot / norms, -1.0, 1.0) if norms != 0 else 1.0
    return np.degrees(np.arccos(cos_theta))

def classify_phase_relationship(angle: float) -> str:
    if angle <= 30:
        return "syn"
    elif 60 <= angle <= 120:
        return "gauche"
    elif 120 <= angle <= 150:
        return "ψ_corridor"
    elif angle >= 150:
        return "anti"
    else:
        return "untuned"

# --- PHASE III: Semantic Highlighting ---

def highlight_semantic_issues(scroll_text: str, base_vector: np.ndarray, glossary: dict) -> Dict[str, List[str]]:
    red, yellow, green = [], [], []
    for term in glossary:
        term_vec = np.zeros(len(glossary))
        if term in scroll_text:
            term_vec[list(glossary).index(term)] = 1.0
            term_vec /= np.linalg.norm(term_vec) if np.linalg.norm(term_vec) != 0 else 1.0
            angle = steric_angle(term_vec, base_vector)
            relation = classify_phase_relationship(angle)
            if relation == "anti":
                red.append(term)
            elif relation == "ψ_corridor" or relation == "gauche":
                yellow.append(term)
            elif relation == "syn":
                green.append(term)
    return {"red_terms": red, "yellow_terms": yellow, "green_terms": green}

# --- PHASE IV: Polar Scroll Mapping ---

def ψ_polar_scrollmap(term_angles: Dict[str, float], title: str = "ψ Steric Phase Map") -> None:
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    for term, angle_deg in term_angles.items():
        angle_rad = np.radians(angle_deg)
        color = 'green' if angle_deg <= 30 else 'orange' if angle_deg <= 150 else 'red'
        ax.plot([angle_rad], [1], 'o', label=term, color=color)
    ax.set_title(title)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    plt.show()

# --- PHASE V: Language Filter and Tuning ---

def ψ_language_filter(text: str, glossary: dict, base_vec: np.ndarray) -> Dict[str, List[str]]:
    return highlight_semantic_issues(text, base_vec, glossary)

def ψ_term_tuner(term: str, glossary: dict) -> List[str]:
    # Simplified: return similar glossary terms (placeholder logic)
    return [alt for alt in glossary if alt != term and term[:3] in alt]

# --- PHASE VI: Meta Instruments ---

def ψ_anchor_train(scrolls: List[str], glossary: dict) -> np.ndarray:
    vectors = [compute_scroll_vector(s, glossary) for s in scrolls]
    stacked = np.stack(vectors)
    mean_vec = np.mean(stacked, axis=0)
    return mean_vec / np.linalg.norm(mean_vec) if np.linalg.norm(mean_vec) != 0 else mean_vec

def ψ_scroll_compare(s1: str, s2: str, glossary: dict) -> Dict[str, float]:
    v1 = compute_scroll_vector(s1, glossary)
    v2 = compute_scroll_vector(s2, glossary)
    angle = steric_angle(v1, v2)
    return {"angle": angle, "class": classify_phase_relationship(angle)}

# --- PHASE VII: Scroll Dissonance Meter ---

def scroll_dissonance_meter(scroll: str, glossary: dict, base_vec: np.ndarray) -> Dict[str, float]:
    sections = scroll.split('\n\n')
    return {
        f'section_{i}': steric_angle(compute_scroll_vector(s, glossary), base_vec)
        for i, s in enumerate(sections)
    }

# --- PHASE VIII: Sigil Suggestion Engine ---

def ψ_sigil_auto_suggester(scroll_text: str, glossary: dict, base_vec: np.ndarray) -> str:
    issues = highlight_semantic_issues(scroll_text, base_vec, glossary)
    if len(issues["red_terms"]) > 5:
        return "☍☉"
    elif len(issues["yellow_terms"]) > 5:
        return "∅→☉"
    elif len(issues["green_terms"]) > 10:
        return "ψ○"
    else:
        return "✿➰( ψ )➿🎼"

# --- END OF psi_semantics.py ---

__all__ = [
    "compute_scroll_vector",
    "steric_angle",
    "classify_phase_relationship",
    "highlight_semantic_issues",
    "ψ_polar_scrollmap",
    "ψ_language_filter",
    "ψ_term_tuner",
    "ψ_anchor_train",
    "ψ_scroll_compare",
    "scroll_dissonance_meter",
    "ψ_sigil_auto_suggester"
]

