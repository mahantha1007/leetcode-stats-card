class Solution:
    def isNumber(self, s: str) -> bool:
        import re
        pattern = re.compile(r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$')
        return bool(pattern.match(s.strip()))
