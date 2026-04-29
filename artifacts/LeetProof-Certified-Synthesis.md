# $\text{LeetProof: Multi-Modal Certified Program Synthesis}$
$\text{arXiv:2604.16584}$

## $\text{Abstract}$
$\text{LeetProof}$ operationalizes **Certified Program Synthesis** (Vericoding) by structuring the workflow around a **Multi-Modal Verifier** ($\text{Velvet}$, embedded in $\text{Lean}$). It resolves the tension between automation (auto-active) and expressivity (interactive) by combining randomized property-based testing for specification validation with delegated proof obligations to frontier AI provers.

## $\text{Architectural Pipeline}$
$$\text{NL}_{\text{desc}} \xrightarrow{\text{SpecSyn}} \text{Spec}_{\text{formal}} \xrightarrow{\text{DynVal}} \text{ValidSpec} \xrightarrow{\text{ProgSyn}} \text{Prog}_{\text{impl}} \xrightarrow{\text{ModalVer}} \text{Proof}_{\text{certified}}$$

### $\text{Key Components}$
1. **$\text{Multi-Modal Verifier (Velvet)}$**: A foundational framework in Lean that integrates:
   - $\text{Dynamic Validation}$: Randomized testing to detect "too weak" or "too strong" specifications.
   - $\text{Automated Proofs}$: High-efficiency verification for simple properties.
   - $\text{Interactive Scripting}$: Expressive proof construction for complex invariants.
2. **$\text{Agentic Pipeline (LeetProof)}$**:
   - $\text{Specification Validation}$: Uncovers defects in reference benchmarks before synthesis.
   - $\text{Decomposition}$: Breaks synthesis into sub-problems guided by verification conditions.
   - $\text{Residual Delegation}$: Offloads hard proof obligations to specialized Lean provers.

## $\text{Flywheel Utility}$
For the **Sovereign Engine**, $\text{LeetProof}$ provides the **Verification Layer** ($\text{VerifLayer}$), ensuring that autonomously generated algorithmic discoveries are mathematically sound, effectively eliminating "Hallucinatory Discovery".
