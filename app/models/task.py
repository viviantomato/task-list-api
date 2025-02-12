from app import db

class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    completed_at = db.Column(db.DateTime, nullable = True) # Can be nullable
    # add foreign key
    goal_id = db.Column(db.Integer, db.ForeignKey('goal.goal_id'), nullable = True) # could be empty
    goal = db.relationship('Goal', back_populates='tasks')

    def to_response(self):
        return {
            "task": self.to_dict()
        }

    def to_dict(self):
        task_dict = {    
                "id":self.task_id,
                "title":self.title,
                "description":self.description,
                "is_complete": True if self.completed_at else False               
        }
        # add condition so goal_id could show when necessary
        if self.goal_id:
            task_dict["goal_id"] = self.goal_id            
        return task_dict
        