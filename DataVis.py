"""z histogram"""
def z_histogram(name):
    output = '//Users/nicholashochmuth/Python/Harvard/compact_galaxies/cg_output/paper_plots'
    plt.hist(cat_z[high_index[0]], bins=50, color='purple')
    plt.xlabel('Z')
    plt.ylabel('Signal Strength')
    plt.title('SDSS Z Histogram')
    plt.savefig(output + name + '.png', dpi = 400)

def specmass_histogram(name):
    output = '//Users/nicholashochmuth/Python/Harvard/compact_galaxies/cg_output/paper_plots'
    #cat['MASS_LP'] = cat_specmass
    plt.hist(cat['MASS_LP'][high_index[0]], bins=50, range=(9.8,12), color='green')
    plt.xlabel('Spectral Mass')
    plt.ylabel('Signal Strength')
    plt.title('SDSS Spectral Mass Histogram')
    plt.savefig(output + name + '.png', dpi = 400)

def save_figures(n):
    output = '//Users/nicholashochmuth/Python/Harvard/compact_galaxies/cg_output/paper_plots'
    read_sdss(cat_file[n], cat_z[n])
    plt.plot(image_data.lam, image_data.flux)
    plt.xlabel('Wavelength (Angstroms)')
    plt.ylabel('Flux')
    plt.title(cat_file[n])
    plt.savefig(output + 'index' + cat_file[n] + '.png', dpi = 400)
    plt.close()
    fitsdss_hdelta2(image_data.lam, image_data.flux, image_data.sigma)
    plt.title(cat_file[n])
    plt.savefig(output + cat_file[n] + '.png', dpi = 400)
    plt.close()