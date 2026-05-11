/// obj_scoreboard : Draw

//location of each bar
var x1  = 8;
var y1  = 8;
var x2  = 256;
var h   = 24;
var gap = 6;

// HP
var hp_val = instance_exists(obj_keyboard) ? obj_keyboard.hp : 0;
var hp_max = instance_exists(obj_keyboard) && variable_instance_exists(obj_keyboard, "max_hp")
             ? obj_keyboard.max_hp : 10; // default max if you haven't added one

draw_healthbar(x1, y1, x2, y1 + h, hp_val, c_black, c_red, c_lime, 0, true, true);

// pXP table
function xp_threshold_for_level(cl) {
    // TOTAL XP needed to level up
    if (cl <= 4) return 400 * cl;
    if (cl <= 8) return 1600 + (cl - 4) * 600;
    return (400 * cl + 100 * sqr(cl - 4)) - 1000;
}

// Levels
var total_xp = global.xp;
var cur_level = 1;
for (var i = 0; i < 200; i++) {
    var next_thresh = xp_threshold_for_level(cur_level);
    if (total_xp < next_thresh) break;
    cur_level++;
}

var prev_thresh = (cur_level == 1) ? 0 : xp_threshold_for_level(cur_level - 1);
var next_thresh = xp_threshold_for_level(cur_level);
var pct = 0;
if (next_thresh > prev_thresh) pct = (total_xp - prev_thresh) / (next_thresh - prev_thresh);
pct = clamp(pct, 0, 1);
//XP bar
var xp_y1 = y1 + h + gap;
draw_healthbar(x1, xp_y1, x2, xp_y1 + h, pct * 100, c_black, c_dkgray, c_aqua, 0, true, true);
//label
draw_set_color(c_white);
draw_text(x1 + 8, y1 + 4, "HP: " + string(hp_val));
draw_text(x1 + 8, xp_y1 + 4, "XP: " + string(total_xp) + " / " + string(next_thresh) + "  (Lvl " + string(cur_level) + ")");
draw_set_alpha(1);