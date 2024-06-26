import random

from hackgen import TestInputFormat, TestGenerator, Language


class InputFormat(TestInputFormat):
    """
    Phần này sẽ sinh các Input tự động và khớp với mô tả của thử thách.
    Các thầy cô có thể tự làm theo cách riêng.
    Tương ứng mỗi dòng trong Input phải in giá trị của nó ra
    """
    __diff = [(1, 10), (1, 20), (-10, 20), (-10, 0), (-20, 20),
              (-50, -1), (-100, -10), (-1000, 1000), (-10000, -1), (-10000, 10000)]

    def inputs(self, difficult_level: int) -> None:
        max_len = (difficult_level + 1) * 5
        seq = range(*self.__diff[difficult_level])
        items = random.sample(seq, max_len if max_len <= len(seq) else len(seq))

        print(max_len)
        print(*items)  # In thành một dòng


input_format = InputFormat()
test_generator = TestGenerator(test_file_count=10,
                               test_input_format=input_format,
                               language=Language.python('output'),
                               name="SimpleArraySum")
test_generator.run()
