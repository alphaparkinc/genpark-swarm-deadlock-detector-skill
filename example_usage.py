import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import SwarmDeadlockDetectorClient

def main():
    client = SwarmDeadlockDetectorClient()
    res = client.detect_and_resolve_deadlocks()
    print("=== Swarm Deadlock Detector Output ===")
    print(f"Monitored Agents: {res['swarm_agents_monitored_count']} | Edges: {res['dependency_edges_analyzed']}")
    print(f"Deadlock Detected: {res['deadlock_detected']} (Liveness: {res['swarm_liveness_score']*100}%)")
    if res['deadlock_detected']:
        print(f"Circular Cycle: {' -> '.join(res['circular_dependency_cycle'])} -> {res['circular_dependency_cycle'][0]}")
        print(f"Preemption Target: {res['preemption_target_agent']}")
        print(f"Action: {res['recommended_recovery_action']}")

if __name__ == '__main__':
    main()
