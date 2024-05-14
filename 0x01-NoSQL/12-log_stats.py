#!/usr/bin/env python3
"""
Provides some stats about Nginx logs stored in MongoDB
"""

def log_stats(mongo_collection):
    """
    Provides some stats about Nginx logs stored in MongoDB
    """
    total_logs = mongo_collection.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: mongo_collection.count_documents({"method": method}) for method in methods}
    status_check_count = mongo_collection.count_documents({"method": "GET", "path": "/status"})
    return total_logs, method_counts, status_check_count
