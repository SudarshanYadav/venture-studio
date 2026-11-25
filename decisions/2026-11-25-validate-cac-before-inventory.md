# 2026-11-25: Validate CAC with smoke tests before buying inventory

**Decision:** No inventory purchase until a smoke test shows customers can be acquired at an affordable cost.

**How:** `playbooks/smoke-test.md`: compute max affordable CAC → refundable paid pre-order landing page → small Meta test (~₹25k/product, ~10 days, ≥25 paid pre-orders) → compare CPO with max CAC (GO ≤70%, ITERATE 70–100%, KILL >100%; small-sample rule at 25 orders).

**Why:** It caps the downside at roughly ₹25k per idea instead of an inventory order, and replaces guessed CPC/CVR with measured numbers.
