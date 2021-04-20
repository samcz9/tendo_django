from rest_framework import parsers


class NestedParser(parsers.FormParser):

    def parse(self, stream, media_type=None, parser_context=None):
        try:
            result = super().parse(
                stream=stream,
                media_type=media_type,
                parser_context=parser_context
            )
            data = {}
            used = []
            for key, value in result.items():
                if '[' in key:
                    first_key = key[:key.index('[')]
                    if first_key not in used:
                        data[first_key] = self.parse_list(
                            [(x[x.index('['):], y) for x, y in result.items(
                            ) if ('[' in x and x[:x.index('[')] == first_key)])
                        used.append(first_key)
                else:
                    if value == 'true' or value == 'false':
                        data[key] = True if value == 'true' else False
                    else:
                        data[key] = value
            return data
        except Exception as e:
            print('Exception:', e)

    def parse_list(self, list1):
        try:
            used = []
            new_list = []
            dict_ret = {}
            for key, value in list1:
                if key == '':
                    if value == 'true' or value == 'false':
                        return True if value == 'true' else False
                    else:
                        return value

                key1 = key[1:key.index(']')]
                if key1 not in used:
                    try:
                        int(key1)
                        new_list.append(self.parse_list(
                            [(x[x.index(']') + 1:], y) for x, y in list1 if (
                                x[1:x.index(']')] == key1)]))
                        used.append(key1)
                    except ValueError:
                        used.append(key1)
                        dict_ret[key1] = self.parse_list(
                                [(x[x.index(']') + 1:],
                                    y) for x, y in list1 if (
                                    x[1:x.index(']')] == key1)])
            if len(dict_ret) != 0:
                return dict_ret
            return new_list
        except Exception as e:
            print('Exception:', e)
