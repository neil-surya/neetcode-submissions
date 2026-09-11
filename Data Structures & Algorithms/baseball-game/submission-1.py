class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record: list = []
        sm = 0
        for operation in operations:
            if operation == '+':
                record.append(record[-1] + record[-2])
            elif operation == 'D':
                record.append(record[-1] * 2)
            elif operation == 'C':
                record.pop()
            else:
                record.append(int(operation))
        for score in record:
            sm += score
        return sm