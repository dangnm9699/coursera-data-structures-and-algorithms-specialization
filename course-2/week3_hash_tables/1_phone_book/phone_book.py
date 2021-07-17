# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]


def write_responses(result):
    print('\n'.join(result))


def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = dict()
    for cur_query in queries:
        q_number = cur_query.number
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            # for contact in contacts:
            #     if contact.number == cur_query.number:
            #         contact.name = cur_query.name
            #         break
            # else:  # otherwise, just add it
            #     contacts.append(cur_query)
            contacts[q_number] = cur_query.name
        elif cur_query.type == 'del':
            # for j in range(len(contacts)):
            #     if contacts[j].number == cur_query.number:
            #         contacts.pop(j)
            #         break
            if q_number in contacts.keys():
                contacts.pop(q_number)
        else:
            response = 'not found'
            # for contact in contacts:
            #     if contact.number == cur_query.number:
            #         response = contact.name
            #         break
            # result.append(response)
            if q_number in contacts.keys():
                response = contacts[q_number]
            result.append(response)
    return result


if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
