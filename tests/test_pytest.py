from matrixregr.matrixregression import MatrixRegression


def test_loading_instance():
    mr = MatrixRegression()

    assert isinstance(mr, MatrixRegression)
