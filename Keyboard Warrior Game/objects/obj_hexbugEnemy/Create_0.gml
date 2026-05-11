/// obj_hexbugEnemy : Create

x = irandom_range(32, room_width - 32);
y = -sprite_get_height(sprite_index) - 16;

progress = 0;
base_speed = 1.5;
damageDone = 1;
word = "";

// Always give a word so drawing/typing doesn't crash
//word = choose("hex", "bug", "type", "key");

/*
// JSON LOAD (disabled until words.json exists)
if (!variable_global_exists("word_list")) {
    global.word_list = [];

    var json_text = string_load("words.json");
    var data = json_parse(json_text);

    if (is_struct(data) && variable_struct_exists(data, "words") && is_array(data.words)) {
        global.word_list = data.words;
    }
}

if (is_array(global.word_list) && array_length(global.word_list) > 0) {
    word = global.word_list[irandom(array_length(global.word_list) - 1)];
}
*/