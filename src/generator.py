from faker import Faker

import pandas as pd


def list_to_data(fake_data, headers):
    return pd.DataFrame.from_records(data=fake_data, columns=headers)


class Generator(object):

    def __init__(self, data):
        self.data = data

    def handler(self):
        resp = self.fake_data()
        first_header = self.data.get('data_gen')[0].get('name')
        resp.set_index(first_header, inplace=True)
        return resp

    def fake_data(self):
        fake = Faker()
        generated_data = []
        header_values = []
        data = self.data.get('data_gen')
        for i in range(len(data)):
            header_values.append(data[i].get('name'))

        for value in range(self.data.get('row_count')):
            data_list = []
            for i in range(len(data)):
                data_type = data[i].get('data_type')
                value_range = data[i].get('range')
                if data_type == 'first_name':
                    data_list.append(fake.unique.first_name())
                elif data_type == 'last_name':
                    data_list.append(fake.unique.last_name())
                elif data_type == 'address':
                    data_list.append(fake.unique.address().replace(",", ""))
                elif data_type == 'zip_code':
                    data_list.append(int(fake.postcode()))
                elif data_type == 'email':
                    data_list.append(fake.unique.email())
                elif data_type == 'phone_number':
                    data_list.append(fake.unique.phone_number())
                elif data_type == 'date_of_birth':
                    data_list.append(str(fake.date_of_birth()))
                elif data_type == 'file_name':
                    data_list.append(str(fake.file_path(depth=5, extension='parquet')))
                elif data_type == 'date':
                    data_list.append(fake.date())
                elif data_type == 'year':
                    data_list.append(fake.year())
                elif data_type == 'month':
                    data_list.append(fake.month())
                elif data_type == 'day':
                    data_list.append(fake.day_of_month())
                elif data_type == 'int':
                    if value_range is None:
                        data_list.append(fake.random_int(min=0, max=9999))
                    else:
                        data_list.append(fake.random_int(min=value_range[0], max=value_range[1]))
                elif data_type == 'decimal':
                    if value_range is None:
                        data_list.append(fake.pydecimal(right_digits=4, positive=True))
                    else:
                        data_list.append(fake.pydecimal(left_digits=value_range[0], right_digits=value_range[1], positive=True))
                else:
                    data_list.append(data_type)

            generated_data.append(data_list)

        return list_to_data(generated_data, header_values)
