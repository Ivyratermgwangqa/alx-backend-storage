#!/usr/bin/env python3
"""
Provides some advanced stats about Nginx logs stored in MongoDB
"""

def log_stats_advanced(mongo_collection):
    """
    Provides some advanced stats about Nginx logs stored in MongoDB
    """
    total_logs = mongo_collection.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: mongo_collection.count_documents({"method": method}) for method in methods}
    status_check_count = mongo_collection.count_documents({"method": "GET", "path": "/status"})
    ip_counts = mongo_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 5}
    ])
    return total_logs, method_counts, status_check_count, list(ip_counts)
