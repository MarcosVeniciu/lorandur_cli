import re
import random
from typing import Tuple, List

class DiceUtils:
    """
    Parser para a notação de dados da engine Lorandur.
    Suporta: XdY, modificadores (+/-), e futuramente khN (Keep Highest).
    """
    
    # Regex simples para capturar "2d6", "1d20+5", "1d100-10"
    _DICE_PATTERN = re.compile(r'(\d+)d(\d+)([\+\-]\d+)?')

    @staticmethod
    def parse_and_roll(formula: str) -> Tuple[int, str]:
        """
        Lê uma string como '2d6+4' e retorna (resultado_int, log_detalhado).
        Se a string for apenas um número '5', retorna (5, 'Fixed').
        """
        formula = formula.strip().lower()
        
        # Caso base: valor fixo
        if formula.isdigit():
            return int(formula), f"Fixed({formula})"

        match = DiceUtils._DICE_PATTERN.match(formula)
        if not match:
            # Fallback seguro
            return 0, f"Error parsing '{formula}'"

        count = int(match.group(1))
        faces = int(match.group(2))
        modifier_str = match.group(3)
        modifier = int(modifier_str) if modifier_str else 0

        rolls = [random.randint(1, faces) for _ in range(count)]
        total = sum(rolls) + modifier

        # Monta string de log: "[3, 5] + 4 = 12"
        log = f"{rolls}{modifier_str if modifier_str else ''} = {total}"
        
        return total, log

    @staticmethod
    def resolve_dynamic_value(value_str: str) -> int:
        """Atalho para pegar apenas o valor numérico final."""
        val, _ = DiceUtils.parse_and_roll(value_str)
        return val