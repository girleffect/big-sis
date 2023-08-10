/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {

  theme: {
    container: {
      center: true,
      padding: {
        DEFAULT: '1.4rem',
        sm: '1.4rem',
        md: '1.2rem',
        lg: '2rem',
        xl: '3rem',
        '2xl': '5rem',
      },

    },

    fontFamily: {
      sans: 'work-sans, sans-serif',
      header: 'bn-dime, sans-serif',
      logo: 'thunder, sans-serif',
      serif: 'fedra-sans, sans-serif',
      // lala : 'fedra-sans, sans-serif',
    },


    extend: {
      animation: {
        fadeInDown: 'fadeInDown .3s ease-in-out',
        fadeOutUp: 'fadeOutUp .3s ease-in-out',
      },
      colors: {
        transparent: 'transparent',
        current: 'currentColor',
        'white': '#ffffff',
        'black': '#312727',
        'gray-300': '#A5A5A5',
        'primary-300': '#8665C6',
        'primary-500': '#633DB3',
        'primary-600': '#633DB3',
        'primary-700': '#095772',
        'dark-section': '#312727',
        'cyan': '#40D0BA',
        'cyan-dark': '#095772', 
        'yellow': '#FFD100',
        'orange': "#FF8100",
        'pink':"#FF7E76",
        'neutral-100': "#F2F1EB"
      },

      screens: {
        'md': '748px',
        'lg': '1024px',
        'xl': '1200px',
        '2xl': '1460px',
        // => @media (min-width: 992px) { ... }
      },
      fontSize: {
        h1: ['40px', '40px'],
        h2: ['34px', '40px'],
        h3: ['32px', '37px'],
        h4: ['24px', '29px'],
        xs: ['12px', '17px'],
        sm: ['16px', '23px'],
        base: ['17px', '26px'],
        lg: ['21px', '32px'],
        xl: ['24px', '34px'],
      },

    },
  },


  content: [
    /**
     * HTML. Paths to Django template files that will contain Tailwind CSS classes.
     */

    /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
    '../templates/**/*.html',

    /*
     * Main templates directory of the project (BASE_DIR/templates).
     * Adjust the following line to match your project structure.
     */
    '../../../templates/**/*.html',

    /*
     * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
     * Adjust the following line to match your project structure.
     */
    '../../**/templates/**/*.html',

    /**
     * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
     * patterns match your project structure.
     */
    /* JS 1: Ignore any JavaScript in node_modules folder. */
    // '!../../**/node_modules',
    /* JS 2: Process all JavaScript files in the project. */
    // '../../**/*.js',

    /**
     * Python: If you use Tailwind CSS classes in Python, uncomment the following line
     * and make sure the pattern below matches your project structure.
     */
    // '../../**/*.py'
  ],
  plugins: [
    /**
     * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
     * for forms. If you don't like it or have own styling for forms,
     * comment the line below to disable '@tailwindcss/forms'.
     */
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
    require('@tailwindcss/line-clamp'),
    require('@tailwindcss/aspect-ratio'),
    //require('tailwindcss-debug-screens'),
  ],
}
