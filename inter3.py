#bank automation logic, handling deposits, withdrawals, cashback after 24 hours, and invalid requests:

class Solution:
    def bank(self, balances:list[int], requests:list[str])->list[int]:
        cashback_schedule = []  # List of (timestamp_due, holder_id, cashback_amount)

        for req in requests:
            parts = req.strip().split()
            if len(parts) != 4:
                continue  # Skip invalid request formats

            action, timestamp_str, holder_str, amount_str = parts

            try:
                timestamp = int(timestamp_str)
                holder_id = int(holder_str) - 1  # Convert 1-based index to 0-based
                amount = int(amount_str)
            except:
                continue  # Invalid number format

            # Apply any cashback due up to and including this timestamp
            new_schedule = []
            for t_due, uid, cb_amt in cashback_schedule:
                if t_due <= timestamp:
                    if 0 <= uid < len(balances):
                        balances[uid] += cb_amt
                else:
                    new_schedule.append((t_due, uid, cb_amt))
            cashback_schedule = new_schedule

            if holder_id < 0 or holder_id >= len(balances):
                continue  # Invalid account

            if action == "deposit":
                balances[holder_id] += amount

            elif action == "withdraw":
                if balances[holder_id] >= amount:
                    balances[holder_id] -= amount
                    cashback = (amount * 2) // 100  # 2% cashback
                    cashback_schedule.append((timestamp + 86400, holder_id, cashback))

        return balances

solution = Solution()
balances = [100, 150]
requests = [
    "deposit 1000 1 50",
    "withdraw 1005 1 30",
    "withdraw 1006 2 50",
    "withdraw 1007 1 40",
    "withdraw 200000 1 50"
]
print(solution.bank(balances, requests))
