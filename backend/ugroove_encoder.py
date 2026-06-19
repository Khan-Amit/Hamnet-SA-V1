# backend/ugroove_encoder.py
# HamNetwork-SA Induction Processor v1.0
# Converts raw WiFi packets into Ternary (U-groove + Compression)

import numpy as np
import hashlib

class UgrooveTernary:
    def __init__(self):
        self.ternary_map = {
            '00': '0',
            '01': '1',
            '10': '2',
            '11': ''   # Noise/Error (ignore)
        }

    def apply_ugroove_smooth(self, raw_signal):
        """
        FIXED U-groove smoothing: Uses weighted majority vote (center weight 2).
        Preserves bits while removing isolated noise.
        """
        # Convert raw bytes to list of ints (0-255)
        bits = []
        for byte in raw_signal:
            bits.extend([int(b) for b in format(byte, '08b')])
        
        smoothed_bits = []
        for i in range(len(bits)):
            center = bits[i]
            left = bits[i-1] if i > 0 else center
            right = bits[i+1] if i < len(bits) - 1 else center
            # Weighted sum: center has weight 2, neighbors weight 1
            total = (center * 2) + left + right
            smoothed_bits.append(1 if total > 2 else 0)
        
        return np.array(smoothed_bits)

    def binary_to_ternary(self, smoothed_bits):
        """Converts smoothed binary bits to Ternary (Base-3) symbols."""
        ternary_output = []
        for i in range(0, len(smoothed_bits) - 1, 2):
            chunk = str(smoothed_bits[i]) + str(smoothed_bits[i+1])
            if chunk in self.ternary_map:
                val = self.ternary_map[chunk]
                if val != '':
                    ternary_output.append(val)
        return ''.join(ternary_output)

    def process_packet(self, raw_packet_data):
        """
        Full pipeline: Smooth → Encode to Ternary → Hash for identification
        """
        # Step 1: Apply U-groove smoothing
        smoothed_bits = self.apply_ugroove_smooth(raw_packet_data)
        
        # Step 2: Convert to Ternary
        ternary_data = self.binary_to_ternary(smoothed_bits)
        
        # Step 3: Generate a unique hash for this packet
        packet_hash = hashlib.sha256(raw_packet_data).hexdigest()[:16]
        
        # Step 4: Stats
        original_size = len(raw_packet_data)
        compressed_size = len(ternary_data)
        ratio = compressed_size / (original_size * 8) if original_size > 0 else 0
        
        # Binary preview for display
        binary_preview = ''.join(str(b) for b in smoothed_bits[:200])
        if len(smoothed_bits) > 200:
            binary_preview += '...'
        
        return {
            "binary_preview": binary_preview,
            "ternary": ternary_data[:200] + ('...' if len(ternary_data) > 200 else ''),
            "original_size": original_size,
            "compressed_size": compressed_size,
            "ratio": round(ratio, 4),
            "hash": packet_hash
        }
