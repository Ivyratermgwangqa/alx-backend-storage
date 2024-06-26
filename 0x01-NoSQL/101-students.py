#!/usr/bin/env python3
"""
Returns all students sorted by average score
"""

def top_students(mongo_collection):
    """
    Returns all students sorted by average score
    """
    students = list(mongo_collection.find({}))
    for student in students:
        scores = [topic['score'] for topic in student['topics']]
        student['averageScore'] = sum(scores) / len(scores)
    return sorted(students, key=lambda x: x['averageScore'], reverse=True)
