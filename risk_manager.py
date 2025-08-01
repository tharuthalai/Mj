def should_exit(current, entry):
    sl = entry * 0.98  # 2% stop loss
    tgt = entry * 1.02 # 2% target
    return current <= sl or current >= tgt
