import pandas as pd
import pkg_resources

def load_cardiac_output_by_organ():
    # This is a stream-like object. If you want the actual info, call
    # stream.read()
    stream = pkg_resources.resource_stream(__name__, 'data/cardiac_output_by_organ.csv')
    return pd.read_csv(stream, encoding='latin-1')
