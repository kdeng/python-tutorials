

import child_module
print(child_module.get_balance())
import another_module
print(child_module.get_balance())
child_module.change_it(10)
print(child_module.get_balance())