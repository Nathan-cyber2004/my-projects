// hexbug spawn logic
spawn_timer++;

if (spawn_timer >= spawn_interval) {
    spawn_timer = 0;
    enemy = instance_create_layer(0, 0, "Instances", obj_hexbugEnemy);
	var r_num = irandom(array_length(word_array) - 1);
	enemy.word = word_array[r_num];
}

// select lowest bug as target
var target = noone;

if (instance_exists(obj_keyboard) && instance_exists(obj_hexbugEnemy)) {
    var best_dist = 1000000000; // <-- use this instead of 1e9
    var count = instance_number(obj_hexbugEnemy);

    for (var i = 0; i < count; i++) {
        var e = instance_find(obj_hexbugEnemy, i);
        if (e != noone) {
            var d = abs(e.y - obj_keyboard.y);
            if (d < best_dist) {
                best_dist = d;
                target = e
				global.target_enemy = target;
            }
        }
    }
}

//type logic
if (target != noone && keyboard_lastkey != 0) {

    var ch = chr(keyboard_lastkey);
    ch = string_lower(ch);

    if (string_length(ch) == 1 && ch >= "a" && ch <= "z") {

        with (target) {
            var expected = string_char_at(word, progress + 1);

            if (ch == expected) {
                progress++;
                if (progress >= string_length(word)) {
                    global.xp += 50;
                    instance_destroy();
                }
            } else {
                progress = 0;
            }
        }
    }

    keyboard_lastkey = 0;
}