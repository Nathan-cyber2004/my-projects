var expected = string_char_at(word, progress + 1);

if (other._typed_letter == expected) {
    progress++;

    // Word finished? Enemy dies and gives XP
    if (progress >= string_length(word)) {
        global.xp += 50; // temporary XP reward (change later)
        instance_destroy();
    }
} else {
    // Mistype resets progress
    progress = 0;
}