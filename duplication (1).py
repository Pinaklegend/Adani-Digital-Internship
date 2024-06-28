
from sentence_transformers import SentenceTransformer
from PIL import Image
import requests
import numpy as np
from sklearn.cluster import DBSCAN
from collections import defaultdict


class find_duplicates():
    def __init__(self, urllist) -> None:
        self.model = SentenceTransformer("clip-ViT-B-32")
        self.urllist = urllist
        self.images_embds = {}

    def load_image(self, url_or_path):
        if url_or_path.startswith("http://") or url_or_path.startswith("https://"):
            return Image.open(requests.get(url_or_path, stream=True).raw)
        else:
            return Image.open(url_or_path)

    def embeddings(self):
        
        # self.images_embds = {image_path.split("/")[-1]: self.model.encode(self.load_image(image_path)) for image_path in self.urllist if str(image_path).split(".")[-1] in ("jpg","png","jpeg")}
        self.images_embds = {image_path: self.model.encode(self.load_image(image_path)) for image_path in self.urllist if str(image_path).split(".")[-1] in ("jpg","png","jpeg")}

    def clustering(self):
        
        clustering = DBSCAN(min_samples=1, eps=2).fit(np.stack(self.images_embds.values()))
        
        image_id_communities = defaultdict(set)
        independent_image_ids = set()

        for image_id, cluster_idx in zip(self.images_embds.keys(), clustering.labels_):
            cluster_idx = int(cluster_idx)
            if cluster_idx == -1:
                independent_image_ids.add(image_id)
                continue

            image_id_communities[cluster_idx].add(image_id)
        return image_id_communities


