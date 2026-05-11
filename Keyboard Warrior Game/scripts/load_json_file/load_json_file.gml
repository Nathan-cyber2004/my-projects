function load_json_file(_filename)
{
    var file = file_text_open_read(_filename);
    var text = "";

    while (!file_text_eof(file)) {
        text += file_text_read_string(file);
        file_text_readln(file);
    }

    file_text_close(file);
    return json_parse(text);
}