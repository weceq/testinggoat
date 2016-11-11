QUnit.test( "errors should be hiddend on keypress", function(assert) {
    hideErrorsOnKeypess();
    var done = assert.async();
    var input = $("input[name='text']");
    console.log(input);
    input.keypress();
    setTimeout(function(){
        assert.ok($(".has-error").is(":hidden"), "Errors are hidden on keypress");
        done();
    });
});

QUnit.test("errors should be visible unless keypress", function(assert) {
    hideErrorsOnKeypess();
    assert.ok($(".has-error").is(":visible"), "Errors are visible");
});
