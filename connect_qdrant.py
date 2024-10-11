from qdrant_client import QdrantClient
from qdrant_client.http import models
from sentence_transformers import SentenceTransformer
import pandas as pd

client = QdrantClient(host='localhost', port=6333)

client.create_collection(
    collection_name="airbnb_listing",
    vectors_config={
        "image": models.VectorParams(size=512, distance=models.Distance.DOT),
        "desctiprion": models.VectorParams(size=256, distance=models.Distance.COSINE),
    },
)


# points = []
# for idx, row in df.iterrows():
#     point = models.PointStruct(
#         id=row['listing_id'],
#         vector=embeddings[idx],
#         payload={
#             "listing_id": row['listing_id'],
#             "host_id": row['host_id'],
#             "price": int(row['price']),
#             "room_type": row['room_type'],
#             "location": {"lat": row['latitude'], "lon": row['longitude']},
#             "number_of_reviews": int(row['number_of_reviews']),
#             "review_scores_rating": float(row['review_scores_rating'])
#         }
#     )
#     points.append(point)

# batch_size = 1000
# for i in range(0, len(points), batch_size):
#     batch = points[i:i + batch_size]
#     client.upsert(collection_name=collection_name, points=batch)
#     print(f"Inserted batch {i // batch_size + 1}")

# def find_similar_listings(listing_id, top_k=5):
#     vector = client.get_vector(collection_name=collection_name, id=listing_id).vector
#     results = client.search(
#         collection_name=collection_name,
#         query_vector=vector,
#         limit=top_k + 1,  # +1 to exclude the query listing itself
#         with_payload=True
#     )
#     similar = [res for res in results if res.id != listing_id][:top_k]
#     return similar

# similar_listings = find_similar_listings('12345', top_k=5)
# for listing in similar_listings:
#     print(f"Listing ID: {listing.id}, Price: {listing.payload['price']}, Room Type: {listing.payload['room_type']}")

# def semantic_search(query, top_k=10):
#     query_vector = model.encode([query])[0]
#     results = client.search(
#         collection_name=collection_name,
#         query_vector=query_vector,
#         limit=top_k,
#         with_payload=True
#     )
#     return results

# # Example usage
# search_results = semantic_search("Cozy apartment near central park", top_k=10)
# for listing in search_results:
#     print(f"Listing ID: {listing.id}, Price: {listing.payload['price']}, Room Type: {listing.payload['room_type']}")

