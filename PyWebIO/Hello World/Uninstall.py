from pywebio.output import *
from pywebio.input import * 
from pip import _internal
from pip._internal.utils.misc import get_installed_distributions
import time
import asyncio

put_markdown('Pip Package Manager')

installed_packages = get_installed_distributions()
installed_packages_set = { package for package in ["%s==%s" % (i.key, i.version)
     for i in installed_packages] }

async def uninstall(package):
    _internal.main(['uninstall', '-y', package])

async def main(package):
    task = asyncio.create_task(uninstall(package))
    completed = False
    counter = 1
    put_text(f"Uninstalling {package}. Please wait until it is removed!")
    put_processbar('bar')
    while not completed:
        counter+=counter
        await asyncio.sleep(1)
        # if the task takes too long reinitiate the counter
        if counter > 10:
           counter = 1
        if task.done():
            completed = True
            counter = 10
            put_markdown(f"Successfully uninstalled {package}")
        else:
            print("waiting...")
        set_processbar('bar', counter / 10)
    
package = select("Choose a package to uninstall", sorted(installed_packages_set))
print("you chose to remove", package)
asyncio.run(main(package))