#!/bin/bash

if [ "$3" != "" ]; then
    if [ "$4" != "" ]; then
            if [ "$1" == "add" ]; then
                /usr/bin/notify-send-all -c device.added -t 3000 -i /usr/share/udev_notify/icons/in.png -u normal "Подключено устройство" "$(echo -e "\nУстройство  '$5' \nVendor id: $4     Device id: $3\nПодключено к ПК!")"
            else
                if [[ "$4" != bus* ]]; then
                    /usr/bin/notify-send-all -c device.removed -t 3000 -i /usr/share/udev_notify/icons/out.png -u normal "Отключено устройство" "$(echo -e "\nУстройство  $(/usr/bin/usb_get_data_by_product.py $3)\nОтключено от ПК!")!"
                fi
            fi
    fi
fi
