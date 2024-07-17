from comfyui_video_helper_suite.videohelpersuite.nodes import get_video_formats


def test_get_video_formats():
    assert len(get_video_formats()) > 0
