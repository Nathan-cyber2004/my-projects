/// obj_hexbugEnemy : Step (bare minimum)
if (instance_exists(obj_keyboard)) {
    if (y < obj_keyboard.y) y += base_speed;
}