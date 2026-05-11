draw_self();

// word above enemy
draw_set_color(c_white);
draw_text(x, y - 32, word);

// typed progress 

var typed = string_copy(word, 1, progress);
draw_set_color(c_aqua);
draw_text(x, y - 32, typed);

//should highlight the targeted enemy
if (variable_global_exists("target_enemy") && id == global.target_enemy) {

    //transparent fill
    draw_set_alpha(0.25);
    draw_set_color(c_fuchsia);
    draw_rectangle(bbox_left - 4, bbox_top - 4, bbox_right + 4, bbox_bottom + 4, false);
	//outline
    draw_set_alpha(1);
    draw_set_color(c_fuchsia);
    for (var t = 0; t < 3; t++) {
        draw_rectangle(bbox_left - t, bbox_top - t, bbox_right + t, bbox_bottom + t, true);
    }

    draw_set_alpha(1);
}