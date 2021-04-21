import os
import shutil

from scale_build.utils.run import run
from scale_build.utils.paths import CHROOT_BASEDIR, TMPFS


def remove_boostrap_directory():
    for command in (
        ['umount', '-f', os.path.join(CHROOT_BASEDIR, 'proc')],
        ['umount', '-f', os.path.join(CHROOT_BASEDIR, 'sys')],
        ['umount', '-f', os.path.join(CHROOT_BASEDIR, 'packages')],
        ['umount', '-f', os.path.join(CHROOT_BASEDIR, 'var/cache/apt')],
        ['umount', '-f', CHROOT_BASEDIR],
        ['umount', '-R', '-f', CHROOT_BASEDIR],
        ['umount', '-R', '-f', TMPFS]
    ):
        run(command, check=False)

    for path in (CHROOT_BASEDIR, TMPFS):
        shutil.rmtree(path, ignore_errors=True)
        os.makedirs(path)
