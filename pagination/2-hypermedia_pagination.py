#!/usr/bin/env python3
"""
This module defines a Server class that paginates a database
of popular baby names, offering both simple index-based
pagination and hypermedia-style pagination with next/previous
page metadata.
"""
import csv
import math
from typing import Dict, List

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initialize a new Server instance with an empty dataset cache.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset.

        Loads the CSV data file the first time it is called, caches
        it as a list of rows (excluding the header row), and returns
        that cached dataset on every subsequent call.

        Returns:
            A list of rows, where each row is itself a list of
            string fields from the CSV file.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a specific page of the dataset.

        Validates that both page and page_size are positive integers,
        then uses index_range to compute the slice of the dataset
        that corresponds to the requested page.

        Args:
            page: The 1-indexed page number to return. Defaults to 1.
            page_size: The number of items per page. Defaults to 10.

        Returns:
            A list of rows for the requested page, or an empty list
            if the requested page is out of range for the dataset.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Retrieve a page of the dataset along with hypermedia metadata.

        Builds on top of get_page to return, in addition to the
        requested page of data, information that helps a client
        navigate the paginated dataset: the current page size, the
        current page number, the next and previous page numbers
        (or None when they don't exist), and the total number of
        pages available.

        Args:
            page: The 1-indexed page number to return. Defaults to 1.
            page_size: The number of items per page. Defaults to 10.

        Returns:
            A dictionary with the keys page_size, page, data,
            next_page, prev_page, and total_pages.
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages,
        }
