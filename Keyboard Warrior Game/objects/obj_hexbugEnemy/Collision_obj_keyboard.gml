if (instance_exists(obj_keyboard) && y >= obj_keyboard.y) {
    if (place_meeting(x, y, obj_keyboard)) {
        var k = instance_place(x, y, obj_keyboard);
        if (k != noone && variable_instance_exists(k, "hp")) {
            k.hp -= damageDone;
        }
        instance_destroy();
        exit;
    }
}