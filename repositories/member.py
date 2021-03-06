from bson.objectid import ObjectId

class MemberRepository:
    def __init__(self, database):
        self._members = database.members

    def add_member(self, member_id, student_id_hash):
        return self._members.insert_one({
            'discordId': member_id,
            'studentIdHash': student_id_hash
        })

    def find_record_for_member(self, member):
        return self._members.find_one({
            'discordId': member.id
        })

    def find_record_for_id(self, id):
        return self._members.find_one({
            '_id': ObjectId(id)
        })

    def find_record_for_student_id_hash(self, hash):
        return self._members.find_one({
            'studentIdHash': hash
        })