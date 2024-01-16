from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from Vectors.Hidden import Qdrant_API_KEY
import numpy as np
import json
from Vectors.Vectors import embedded_query
from Vectors.Vectors import text2

client = QdrantClient("localhost", port=6333)

qdrant_client = QdrantClient(
    "https://29b7abb9-dd18-450c-8e2b-706de38ba80b.us-east4-0.gcp.cloud.qdrant.io:6333",
    api_key=Qdrant_API_KEY,
)



# Here we load all vectors into memory, numpy array works as iterable for itself.
# Other option would be to use Mmap, if we don't want to load all data into RAM
vectors = np.load('./startup_vectors.npy')

qdrant_client.upload_collection(
    collection_name='startups',
    vectors=embedded_query,
    payload=text2,
    ids=None,  # Vector ids will be assigned automatically
    batch_size=256  # How many vectors will be uploaded in a single request?
)
