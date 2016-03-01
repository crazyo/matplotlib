import matplotlib.pyplot as plt
from matplotlib.testing.decorators import image_comparison

@image_comparison(baseline_images=['hyphen_math'],
                  extensions=['png'])
def test_hyphen_in_math():
	text = u'${-}$'
	plt.text(0.5, 0.5, text)


@image_comparison(baseline_images=['hyphen_non_math'],
                  extensions=['png'])
def test_hyphen_in_nonmath():
	text = u'-'
	plt.text(0.5, 0.5, text)



@image_comparison(baseline_images=['hyphen_mixed'],
                  extensions=['png'])
def test_hyphen_in_mixed():
	text = u'math part: ${-}$; non-math part: -'
	plt.text(0.5, 0.5, text)

text = u'${-}$'
plt.text(0.5, 0.5, text)
plt.show()
