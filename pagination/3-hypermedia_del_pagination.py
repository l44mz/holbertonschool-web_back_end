#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initialize a new Server instance with empty dataset caches.
        """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(
            self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieve a page of the dataset that is resilient to deletions.

        Walks the indexed dataset starting at the given index and
        collects page_size available rows, skipping over any indexes
        that no longer exist because their rows were removed. This
        way, a client that keeps requesting the returned next_index
        will not skip or repeat items even if rows are deleted from
        the dataset between requests.

        Args:
            index: The starting index to query from. Defaults to 0
                when None is given.
            page_size: The number of items to return. Defaults to 10.

        Returns:
            A dictionary with the keys index, data, page_size, and
            next_index.
        """
        data = self.indexed_dataset()
        dataset_len = len(self.dataset())

        if index is None:
            index = 0

        assert isinstance(index, int) and 0 <= index < dataset_len

        page_data = []
        current_index = index

        while len(page_data) < page_size and current_index < dataset_len:
            row = data.get(current_index)
            if row is not None:
                page_data.append(row)
            current_index += 1

        return {
            'index': index,
            'data': page_data,
            'page_size': len(page_data),
            'next_index': current_index,
        }
