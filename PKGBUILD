# Udev Notify
# Maintainer: indir <joinmark60@gmail.com>
pkgname=UdevNotify
pkgver=1.1
pkgrel=1
arch=('i686' 'x86_64')
pkgdesc="Udev Notify script"
license=('GPL')
depends=('python')
source=("git+https://github.com/cropinghigh/udev_notify")
md5sums=('SKIP')

package() {
    cd "${srcdir}/${pkgname}"
    mkdir -p $pkgdir/usr/bin/
    mkdir -p $pkgdir/etc/udev/rules.d/
    mkdir -p $pkgdir/usr/share/udev_notify/
    cp notify-send-all $pkgdir/usr/bin/notify-send-all
    cp udev_notify.sh $pkgdir/usr/bin/udev_notify.sh
    cp udev_notify.rules $pkgdir/etc/udev/rules.d/99-udev_notify.rules
    cp usb_get_data_by_product.py $pkgdir/usr/bin/usb_get_data_by_product.py
    cp -r icons $pkgdir/usr/share/udev_notify/
}
