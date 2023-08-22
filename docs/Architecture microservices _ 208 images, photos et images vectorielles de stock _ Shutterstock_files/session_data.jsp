
window.usi_session_data = {
    ip:'154.72.169.125',
    country :'cm'
}
usi_set_session_data = function() {
    if (typeof(usi_app) !== "undefined") {
        usi_app.session_data = window.usi_session_data;
        usi_cookies.set_json("usi_session_data", usi_app.session_data, 24*60*60);
        if (typeof(usi_app.session_data_callback) !== "undefined") {
            usi_app.session_data_callback();
        }
    } else {
        setTimeout(usi_set_session_data, 500);
    }
};
usi_set_session_data();
