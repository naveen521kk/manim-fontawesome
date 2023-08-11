# Automatically generated using scripts/update.py. Don't edit.

# Copyright Naveen M K
#
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE.txt file.

import os

from pathlib import Path
from enum import Enum
from manim import SVGMobject, config, BLACK, WHITE

__all__ = ["brand", "regular", "solid", "FONT_AWESOME_VERSION"]

svg_dir = Path(__file__).parent / 'font-awesome'/ 'svgs'
brand_dir = svg_dir / 'brands'
regular_dir = svg_dir / 'regular'
solid_dir = svg_dir / 'solid'
FONT_AWESOME_VERSION = '6.4.2'


class _Brand(Enum):
  
    unity = os.fspath(brand_dir / 'unity.svg')
  
    drupal = os.fspath(brand_dir / 'drupal.svg')
  
    pied_piper_alt = os.fspath(brand_dir / 'pied-piper-alt.svg')
  
    yahoo = os.fspath(brand_dir / 'yahoo.svg')
  
    stackpath = os.fspath(brand_dir / 'stackpath.svg')
  
    uikit = os.fspath(brand_dir / 'uikit.svg')
  
    bluetooth = os.fspath(brand_dir / 'bluetooth.svg')
  
    node_js = os.fspath(brand_dir / 'node-js.svg')
  
    google = os.fspath(brand_dir / 'google.svg')
  
    aviato = os.fspath(brand_dir / 'aviato.svg')
  
    symfony = os.fspath(brand_dir / 'symfony.svg')
  
    sass = os.fspath(brand_dir / 'sass.svg')
  
    css3_alt = os.fspath(brand_dir / 'css3-alt.svg')
  
    debian = os.fspath(brand_dir / 'debian.svg')
  
    schlix = os.fspath(brand_dir / 'schlix.svg')
  
    glide_g = os.fspath(brand_dir / 'glide-g.svg')
  
    draft2digital = os.fspath(brand_dir / 'draft2digital.svg')
  
    instalod = os.fspath(brand_dir / 'instalod.svg')
  
    creative_commons_sampling_plus = os.fspath(brand_dir / 'creative-commons-sampling-plus.svg')
  
    yoast = os.fspath(brand_dir / 'yoast.svg')
  
    google_plus_g = os.fspath(brand_dir / 'google-plus-g.svg')
  
    tencent_weibo = os.fspath(brand_dir / 'tencent-weibo.svg')
  
    uber = os.fspath(brand_dir / 'uber.svg')
  
    php = os.fspath(brand_dir / 'php.svg')
  
    ns8 = os.fspath(brand_dir / 'ns8.svg')
  
    medium = os.fspath(brand_dir / 'medium.svg')
  
    buysellads = os.fspath(brand_dir / 'buysellads.svg')
  
    trade_federation = os.fspath(brand_dir / 'trade-federation.svg')
  
    vuejs = os.fspath(brand_dir / 'vuejs.svg')
  
    vk = os.fspath(brand_dir / 'vk.svg')
  
    blogger = os.fspath(brand_dir / 'blogger.svg')
  
    vimeo = os.fspath(brand_dir / 'vimeo.svg')
  
    osi = os.fspath(brand_dir / 'osi.svg')
  
    stubber = os.fspath(brand_dir / 'stubber.svg')
  
    fort_awesome_alt = os.fspath(brand_dir / 'fort-awesome-alt.svg')
  
    vaadin = os.fspath(brand_dir / 'vaadin.svg')
  
    bots = os.fspath(brand_dir / 'bots.svg')
  
    gratipay = os.fspath(brand_dir / 'gratipay.svg')
  
    adn = os.fspath(brand_dir / 'adn.svg')
  
    deskpro = os.fspath(brand_dir / 'deskpro.svg')
  
    wpforms = os.fspath(brand_dir / 'wpforms.svg')
  
    slideshare = os.fspath(brand_dir / 'slideshare.svg')
  
    yandex = os.fspath(brand_dir / 'yandex.svg')
  
    patreon = os.fspath(brand_dir / 'patreon.svg')
  
    creative_commons_sa = os.fspath(brand_dir / 'creative-commons-sa.svg')
  
    asymmetrik = os.fspath(brand_dir / 'asymmetrik.svg')
  
    stack_exchange = os.fspath(brand_dir / 'stack-exchange.svg')
  
    python = os.fspath(brand_dir / 'python.svg')
  
    stack_overflow = os.fspath(brand_dir / 'stack-overflow.svg')
  
    amilia = os.fspath(brand_dir / 'amilia.svg')
  
    figma = os.fspath(brand_dir / 'figma.svg')
  
    get_pocket = os.fspath(brand_dir / 'get-pocket.svg')
  
    searchengin = os.fspath(brand_dir / 'searchengin.svg')
  
    staylinked = os.fspath(brand_dir / 'staylinked.svg')
  
    creative_commons_nc_jp = os.fspath(brand_dir / 'creative-commons-nc-jp.svg')
  
    grunt = os.fspath(brand_dir / 'grunt.svg')
  
    resolving = os.fspath(brand_dir / 'resolving.svg')
  
    bootstrap = os.fspath(brand_dir / 'bootstrap.svg')
  
    fly = os.fspath(brand_dir / 'fly.svg')
  
    blackberry = os.fspath(brand_dir / 'blackberry.svg')
  
    bity = os.fspath(brand_dir / 'bity.svg')
  
    hubspot = os.fspath(brand_dir / 'hubspot.svg')
  
    diaspora = os.fspath(brand_dir / 'diaspora.svg')
  
    apple = os.fspath(brand_dir / 'apple.svg')
  
    fulcrum = os.fspath(brand_dir / 'fulcrum.svg')
  
    orcid = os.fspath(brand_dir / 'orcid.svg')
  
    gofore = os.fspath(brand_dir / 'gofore.svg')
  
    perbyte = os.fspath(brand_dir / 'perbyte.svg')
  
    kickstarter_k = os.fspath(brand_dir / 'kickstarter-k.svg')
  
    meetup = os.fspath(brand_dir / 'meetup.svg')
  
    galactic_senate = os.fspath(brand_dir / 'galactic-senate.svg')
  
    xing = os.fspath(brand_dir / 'xing.svg')
  
    microsoft = os.fspath(brand_dir / 'microsoft.svg')
  
    creative_commons_nc_eu = os.fspath(brand_dir / 'creative-commons-nc-eu.svg')
  
    cloudsmith = os.fspath(brand_dir / 'cloudsmith.svg')
  
    square_js = os.fspath(brand_dir / 'square-js.svg')
  
    square_viadeo = os.fspath(brand_dir / 'square-viadeo.svg')
  
    html5 = os.fspath(brand_dir / 'html5.svg')
  
    the_red_yeti = os.fspath(brand_dir / 'the-red-yeti.svg')
  
    ello = os.fspath(brand_dir / 'ello.svg')
  
    servicestack = os.fspath(brand_dir / 'servicestack.svg')
  
    uncharted = os.fspath(brand_dir / 'uncharted.svg')
  
    angular = os.fspath(brand_dir / 'angular.svg')
  
    uniregistry = os.fspath(brand_dir / 'uniregistry.svg')
  
    affiliatetheme = os.fspath(brand_dir / 'affiliatetheme.svg')
  
    twitter = os.fspath(brand_dir / 'twitter.svg')
  
    monero = os.fspath(brand_dir / 'monero.svg')
  
    d_and_d = os.fspath(brand_dir / 'd-and-d.svg')
  
    mailchimp = os.fspath(brand_dir / 'mailchimp.svg')
  
    contao = os.fspath(brand_dir / 'contao.svg')
  
    black_tie = os.fspath(brand_dir / 'black-tie.svg')
  
    square_gitlab = os.fspath(brand_dir / 'square-gitlab.svg')
  
    free_code_camp = os.fspath(brand_dir / 'free-code-camp.svg')
  
    imdb = os.fspath(brand_dir / 'imdb.svg')
  
    researchgate = os.fspath(brand_dir / 'researchgate.svg')
  
    elementor = os.fspath(brand_dir / 'elementor.svg')
  
    wpbeginner = os.fspath(brand_dir / 'wpbeginner.svg')
  
    square_vimeo = os.fspath(brand_dir / 'square-vimeo.svg')
  
    odysee = os.fspath(brand_dir / 'odysee.svg')
  
    firefox = os.fspath(brand_dir / 'firefox.svg')
  
    gg_circle = os.fspath(brand_dir / 'gg-circle.svg')
  
    fedora = os.fspath(brand_dir / 'fedora.svg')
  
    x_twitter = os.fspath(brand_dir / 'x-twitter.svg')
  
    apper = os.fspath(brand_dir / 'apper.svg')
  
    npm = os.fspath(brand_dir / 'npm.svg')
  
    soundcloud = os.fspath(brand_dir / 'soundcloud.svg')
  
    square_dribbble = os.fspath(brand_dir / 'square-dribbble.svg')
  
    old_republic = os.fspath(brand_dir / 'old-republic.svg')
  
    ember = os.fspath(brand_dir / 'ember.svg')
  
    strava = os.fspath(brand_dir / 'strava.svg')
  
    invision = os.fspath(brand_dir / 'invision.svg')
  
    facebook = os.fspath(brand_dir / 'facebook.svg')
  
    viber = os.fspath(brand_dir / 'viber.svg')
  
    studiovinari = os.fspath(brand_dir / 'studiovinari.svg')
  
    canadian_maple_leaf = os.fspath(brand_dir / 'canadian-maple-leaf.svg')
  
    snapchat = os.fspath(brand_dir / 'snapchat.svg')
  
    sticker_mule = os.fspath(brand_dir / 'sticker-mule.svg')
  
    flipboard = os.fspath(brand_dir / 'flipboard.svg')
  
    ubuntu = os.fspath(brand_dir / 'ubuntu.svg')
  
    opencart = os.fspath(brand_dir / 'opencart.svg')
  
    dashcube = os.fspath(brand_dir / 'dashcube.svg')
  
    pied_piper = os.fspath(brand_dir / 'pied-piper.svg')
  
    jira = os.fspath(brand_dir / 'jira.svg')
  
    btc = os.fspath(brand_dir / 'btc.svg')
  
    chromecast = os.fspath(brand_dir / 'chromecast.svg')
  
    square_pinterest = os.fspath(brand_dir / 'square-pinterest.svg')
  
    hashnode = os.fspath(brand_dir / 'hashnode.svg')
  
    keybase = os.fspath(brand_dir / 'keybase.svg')
  
    github_alt = os.fspath(brand_dir / 'github-alt.svg')
  
    codepen = os.fspath(brand_dir / 'codepen.svg')
  
    mix = os.fspath(brand_dir / 'mix.svg')
  
    firstdraft = os.fspath(brand_dir / 'firstdraft.svg')
  
    foursquare = os.fspath(brand_dir / 'foursquare.svg')
  
    fantasy_flight_games = os.fspath(brand_dir / 'fantasy-flight-games.svg')
  
    buromobelexperte = os.fspath(brand_dir / 'buromobelexperte.svg')
  
    cc_amazon_pay = os.fspath(brand_dir / 'cc-amazon-pay.svg')
  
    vimeo_v = os.fspath(brand_dir / 'vimeo-v.svg')
  
    sketch = os.fspath(brand_dir / 'sketch.svg')
  
    google_pay = os.fspath(brand_dir / 'google-pay.svg')
  
    houzz = os.fspath(brand_dir / 'houzz.svg')
  
    artstation = os.fspath(brand_dir / 'artstation.svg')
  
    app_store_ios = os.fspath(brand_dir / 'app-store-ios.svg')
  
    wix = os.fspath(brand_dir / 'wix.svg')
  
    forumbee = os.fspath(brand_dir / 'forumbee.svg')
  
    mastodon = os.fspath(brand_dir / 'mastodon.svg')
  
    bandcamp = os.fspath(brand_dir / 'bandcamp.svg')
  
    gitkraken = os.fspath(brand_dir / 'gitkraken.svg')
  
    markdown = os.fspath(brand_dir / 'markdown.svg')
  
    pied_piper_hat = os.fspath(brand_dir / 'pied-piper-hat.svg')
  
    line = os.fspath(brand_dir / 'line.svg')
  
    wirsindhandwerk = os.fspath(brand_dir / 'wirsindhandwerk.svg')
  
    linode = os.fspath(brand_dir / 'linode.svg')
  
    rocketchat = os.fspath(brand_dir / 'rocketchat.svg')
  
    cc_diners_club = os.fspath(brand_dir / 'cc-diners-club.svg')
  
    kickstarter = os.fspath(brand_dir / 'kickstarter.svg')
  
    cotton_bureau = os.fspath(brand_dir / 'cotton-bureau.svg')
  
    creative_commons_nc = os.fspath(brand_dir / 'creative-commons-nc.svg')
  
    square_font_awesome = os.fspath(brand_dir / 'square-font-awesome.svg')
  
    medrt = os.fspath(brand_dir / 'medrt.svg')
  
    redhat = os.fspath(brand_dir / 'redhat.svg')
  
    creative_commons_pd_alt = os.fspath(brand_dir / 'creative-commons-pd-alt.svg')
  
    qq = os.fspath(brand_dir / 'qq.svg')
  
    ravelry = os.fspath(brand_dir / 'ravelry.svg')
  
    youtube = os.fspath(brand_dir / 'youtube.svg')
  
    autoprefixer = os.fspath(brand_dir / 'autoprefixer.svg')
  
    buffer = os.fspath(brand_dir / 'buffer.svg')
  
    guilded = os.fspath(brand_dir / 'guilded.svg')
  
    watchman_monitoring = os.fspath(brand_dir / 'watchman-monitoring.svg')
  
    rust = os.fspath(brand_dir / 'rust.svg')
  
    battle_net = os.fspath(brand_dir / 'battle-net.svg')
  
    weebly = os.fspath(brand_dir / 'weebly.svg')
  
    yammer = os.fspath(brand_dir / 'yammer.svg')
  
    zhihu = os.fspath(brand_dir / 'zhihu.svg')
  
    yelp = os.fspath(brand_dir / 'yelp.svg')
  
    maxcdn = os.fspath(brand_dir / 'maxcdn.svg')
  
    jedi_order = os.fspath(brand_dir / 'jedi-order.svg')
  
    square_behance = os.fspath(brand_dir / 'square-behance.svg')
  
    themeisle = os.fspath(brand_dir / 'themeisle.svg')
  
    salesforce = os.fspath(brand_dir / 'salesforce.svg')
  
    untappd = os.fspath(brand_dir / 'untappd.svg')
  
    apple_pay = os.fspath(brand_dir / 'apple-pay.svg')
  
    earlybirds = os.fspath(brand_dir / 'earlybirds.svg')
  
    shopify = os.fspath(brand_dir / 'shopify.svg')
  
    connectdevelop = os.fspath(brand_dir / 'connectdevelop.svg')
  
    first_order = os.fspath(brand_dir / 'first-order.svg')
  
    discourse = os.fspath(brand_dir / 'discourse.svg')
  
    goodreads_g = os.fspath(brand_dir / 'goodreads-g.svg')
  
    stripe_s = os.fspath(brand_dir / 'stripe-s.svg')
  
    cc_jcb = os.fspath(brand_dir / 'cc-jcb.svg')
  
    react = os.fspath(brand_dir / 'react.svg')
  
    napster = os.fspath(brand_dir / 'napster.svg')
  
    centos = os.fspath(brand_dir / 'centos.svg')
  
    square_git = os.fspath(brand_dir / 'square-git.svg')
  
    less = os.fspath(brand_dir / 'less.svg')
  
    mixer = os.fspath(brand_dir / 'mixer.svg')
  
    glide = os.fspath(brand_dir / 'glide.svg')
  
    angrycreative = os.fspath(brand_dir / 'angrycreative.svg')
  
    dhl = os.fspath(brand_dir / 'dhl.svg')
  
    mendeley = os.fspath(brand_dir / 'mendeley.svg')
  
    renren = os.fspath(brand_dir / 'renren.svg')
  
    creative_commons = os.fspath(brand_dir / 'creative-commons.svg')
  
    threads = os.fspath(brand_dir / 'threads.svg')
  
    safari = os.fspath(brand_dir / 'safari.svg')
  
    spotify = os.fspath(brand_dir / 'spotify.svg')
  
    evernote = os.fspath(brand_dir / 'evernote.svg')
  
    gitter = os.fspath(brand_dir / 'gitter.svg')
  
    facebook_f = os.fspath(brand_dir / 'facebook-f.svg')
  
    nimblr = os.fspath(brand_dir / 'nimblr.svg')
  
    google_plus = os.fspath(brand_dir / 'google-plus.svg')
  
    square_facebook = os.fspath(brand_dir / 'square-facebook.svg')
  
    wordpress = os.fspath(brand_dir / 'wordpress.svg')
  
    page4 = os.fspath(brand_dir / 'page4.svg')
  
    sith = os.fspath(brand_dir / 'sith.svg')
  
    _42_group = os.fspath(brand_dir / '42-group.svg')
  
    playstation = os.fspath(brand_dir / 'playstation.svg')
  
    shopware = os.fspath(brand_dir / 'shopware.svg')
  
    laravel = os.fspath(brand_dir / 'laravel.svg')
  
    cloudscale = os.fspath(brand_dir / 'cloudscale.svg')
  
    square_instagram = os.fspath(brand_dir / 'square-instagram.svg')
  
    app_store = os.fspath(brand_dir / 'app-store.svg')
  
    edge = os.fspath(brand_dir / 'edge.svg')
  
    intercom = os.fspath(brand_dir / 'intercom.svg')
  
    scribd = os.fspath(brand_dir / 'scribd.svg')
  
    dev = os.fspath(brand_dir / 'dev.svg')
  
    creative_commons_share = os.fspath(brand_dir / 'creative-commons-share.svg')
  
    google_play = os.fspath(brand_dir / 'google-play.svg')
  
    nfc_directional = os.fspath(brand_dir / 'nfc-directional.svg')
  
    wizards_of_the_coast = os.fspath(brand_dir / 'wizards-of-the-coast.svg')
  
    hacker_news = os.fspath(brand_dir / 'hacker-news.svg')
  
    linux = os.fspath(brand_dir / 'linux.svg')
  
    creative_commons_remix = os.fspath(brand_dir / 'creative-commons-remix.svg')
  
    palfed = os.fspath(brand_dir / 'palfed.svg')
  
    bimobject = os.fspath(brand_dir / 'bimobject.svg')
  
    reacteurope = os.fspath(brand_dir / 'reacteurope.svg')
  
    pied_piper_pp = os.fspath(brand_dir / 'pied-piper-pp.svg')
  
    sellcast = os.fspath(brand_dir / 'sellcast.svg')
  
    empire = os.fspath(brand_dir / 'empire.svg')
  
    viadeo = os.fspath(brand_dir / 'viadeo.svg')
  
    pushed = os.fspath(brand_dir / 'pushed.svg')
  
    hooli = os.fspath(brand_dir / 'hooli.svg')
  
    delicious = os.fspath(brand_dir / 'delicious.svg')
  
    gulp = os.fspath(brand_dir / 'gulp.svg')
  
    nfc_symbol = os.fspath(brand_dir / 'nfc-symbol.svg')
  
    y_combinator = os.fspath(brand_dir / 'y-combinator.svg')
  
    angellist = os.fspath(brand_dir / 'angellist.svg')
  
    creative_commons_pd = os.fspath(brand_dir / 'creative-commons-pd.svg')
  
    cc_paypal = os.fspath(brand_dir / 'cc-paypal.svg')
  
    space_awesome = os.fspath(brand_dir / 'space-awesome.svg')
  
    js = os.fspath(brand_dir / 'js.svg')
  
    java = os.fspath(brand_dir / 'java.svg')
  
    phoenix_framework = os.fspath(brand_dir / 'phoenix-framework.svg')
  
    tumblr = os.fspath(brand_dir / 'tumblr.svg')
  
    suse = os.fspath(brand_dir / 'suse.svg')
  
    reddit = os.fspath(brand_dir / 'reddit.svg')
  
    square_hacker_news = os.fspath(brand_dir / 'square-hacker-news.svg')
  
    cc_discover = os.fspath(brand_dir / 'cc-discover.svg')
  
    mizuni = os.fspath(brand_dir / 'mizuni.svg')
  
    sellsy = os.fspath(brand_dir / 'sellsy.svg')
  
    bitbucket = os.fspath(brand_dir / 'bitbucket.svg')
  
    envira = os.fspath(brand_dir / 'envira.svg')
  
    hotjar = os.fspath(brand_dir / 'hotjar.svg')
  
    linkedin = os.fspath(brand_dir / 'linkedin.svg')
  
    speaker_deck = os.fspath(brand_dir / 'speaker-deck.svg')
  
    buy_n_large = os.fspath(brand_dir / 'buy-n-large.svg')
  
    _500px = os.fspath(brand_dir / '500px.svg')
  
    xbox = os.fspath(brand_dir / 'xbox.svg')
  
    paypal = os.fspath(brand_dir / 'paypal.svg')
  
    itunes_note = os.fspath(brand_dir / 'itunes-note.svg')
  
    square_whatsapp = os.fspath(brand_dir / 'square-whatsapp.svg')
  
    centercode = os.fspath(brand_dir / 'centercode.svg')
  
    vine = os.fspath(brand_dir / 'vine.svg')
  
    twitch = os.fspath(brand_dir / 'twitch.svg')
  
    discord = os.fspath(brand_dir / 'discord.svg')
  
    creative_commons_zero = os.fspath(brand_dir / 'creative-commons-zero.svg')
  
    square_font_awesome_stroke = os.fspath(brand_dir / 'square-font-awesome-stroke.svg')
  
    facebook_messenger = os.fspath(brand_dir / 'facebook-messenger.svg')
  
    docker = os.fspath(brand_dir / 'docker.svg')
  
    accessible_icon = os.fspath(brand_dir / 'accessible-icon.svg')
  
    microblog = os.fspath(brand_dir / 'microblog.svg')
  
    swift = os.fspath(brand_dir / 'swift.svg')
  
    nutritionix = os.fspath(brand_dir / 'nutritionix.svg')
  
    rockrms = os.fspath(brand_dir / 'rockrms.svg')
  
    codiepie = os.fspath(brand_dir / 'codiepie.svg')
  
    cc_apple_pay = os.fspath(brand_dir / 'cc-apple-pay.svg')
  
    quora = os.fspath(brand_dir / 'quora.svg')
  
    raspberry_pi = os.fspath(brand_dir / 'raspberry-pi.svg')
  
    grav = os.fspath(brand_dir / 'grav.svg')
  
    square_pied_piper = os.fspath(brand_dir / 'square-pied-piper.svg')
  
    optin_monster = os.fspath(brand_dir / 'optin-monster.svg')
  
    flickr = os.fspath(brand_dir / 'flickr.svg')
  
    pix = os.fspath(brand_dir / 'pix.svg')
  
    sistrix = os.fspath(brand_dir / 'sistrix.svg')
  
    periscope = os.fspath(brand_dir / 'periscope.svg')
  
    vnv = os.fspath(brand_dir / 'vnv.svg')
  
    think_peaks = os.fspath(brand_dir / 'think-peaks.svg')
  
    yarn = os.fspath(brand_dir / 'yarn.svg')
  
    fonticons_fi = os.fspath(brand_dir / 'fonticons-fi.svg')
  
    sitrox = os.fspath(brand_dir / 'sitrox.svg')
  
    square_reddit = os.fspath(brand_dir / 'square-reddit.svg')
  
    square_github = os.fspath(brand_dir / 'square-github.svg')
  
    meta = os.fspath(brand_dir / 'meta.svg')
  
    joget = os.fspath(brand_dir / 'joget.svg')
  
    typo3 = os.fspath(brand_dir / 'typo3.svg')
  
    readme = os.fspath(brand_dir / 'readme.svg')
  
    squarespace = os.fspath(brand_dir / 'squarespace.svg')
  
    internet_explorer = os.fspath(brand_dir / 'internet-explorer.svg')
  
    korvue = os.fspath(brand_dir / 'korvue.svg')
  
    unsplash = os.fspath(brand_dir / 'unsplash.svg')
  
    cpanel = os.fspath(brand_dir / 'cpanel.svg')
  
    weixin = os.fspath(brand_dir / 'weixin.svg')
  
    pinterest = os.fspath(brand_dir / 'pinterest.svg')
  
    sourcetree = os.fspath(brand_dir / 'sourcetree.svg')
  
    github = os.fspath(brand_dir / 'github.svg')
  
    creative_commons_by = os.fspath(brand_dir / 'creative-commons-by.svg')
  
    supple = os.fspath(brand_dir / 'supple.svg')
  
    stripe = os.fspath(brand_dir / 'stripe.svg')
  
    steam_symbol = os.fspath(brand_dir / 'steam-symbol.svg')
  
    openid = os.fspath(brand_dir / 'openid.svg')
  
    wpexplorer = os.fspath(brand_dir / 'wpexplorer.svg')
  
    square_google_plus = os.fspath(brand_dir / 'square-google-plus.svg')
  
    skyatlas = os.fspath(brand_dir / 'skyatlas.svg')
  
    square_xing = os.fspath(brand_dir / 'square-xing.svg')
  
    lyft = os.fspath(brand_dir / 'lyft.svg')
  
    phabricator = os.fspath(brand_dir / 'phabricator.svg')
  
    edge_legacy = os.fspath(brand_dir / 'edge-legacy.svg')
  
    hackerrank = os.fspath(brand_dir / 'hackerrank.svg')
  
    whmcs = os.fspath(brand_dir / 'whmcs.svg')
  
    stumbleupon_circle = os.fspath(brand_dir / 'stumbleupon-circle.svg')
  
    wordpress_simple = os.fspath(brand_dir / 'wordpress-simple.svg')
  
    creative_commons_nd = os.fspath(brand_dir / 'creative-commons-nd.svg')
  
    fonticons = os.fspath(brand_dir / 'fonticons.svg')
  
    slack = os.fspath(brand_dir / 'slack.svg')
  
    cc_stripe = os.fspath(brand_dir / 'cc-stripe.svg')
  
    wolf_pack_battalion = os.fspath(brand_dir / 'wolf-pack-battalion.svg')
  
    google_drive = os.fspath(brand_dir / 'google-drive.svg')
  
    screenpal = os.fspath(brand_dir / 'screenpal.svg')
  
    deploydog = os.fspath(brand_dir / 'deploydog.svg')
  
    digital_ocean = os.fspath(brand_dir / 'digital-ocean.svg')
  
    rebel = os.fspath(brand_dir / 'rebel.svg')
  
    pinterest_p = os.fspath(brand_dir / 'pinterest-p.svg')
  
    skype = os.fspath(brand_dir / 'skype.svg')
  
    amazon_pay = os.fspath(brand_dir / 'amazon-pay.svg')
  
    speakap = os.fspath(brand_dir / 'speakap.svg')
  
    git = os.fspath(brand_dir / 'git.svg')
  
    usb = os.fspath(brand_dir / 'usb.svg')
  
    airbnb = os.fspath(brand_dir / 'airbnb.svg')
  
    replyd = os.fspath(brand_dir / 'replyd.svg')
  
    avianex = os.fspath(brand_dir / 'avianex.svg')
  
    cc_amex = os.fspath(brand_dir / 'cc-amex.svg')
  
    windows = os.fspath(brand_dir / 'windows.svg')
  
    dailymotion = os.fspath(brand_dir / 'dailymotion.svg')
  
    freebsd = os.fspath(brand_dir / 'freebsd.svg')
  
    fort_awesome = os.fspath(brand_dir / 'fort-awesome.svg')
  
    medapps = os.fspath(brand_dir / 'medapps.svg')
  
    aws = os.fspath(brand_dir / 'aws.svg')
  
    square_twitter = os.fspath(brand_dir / 'square-twitter.svg')
  
    padlet = os.fspath(brand_dir / 'padlet.svg')
  
    kaggle = os.fspath(brand_dir / 'kaggle.svg')
  
    atlassian = os.fspath(brand_dir / 'atlassian.svg')
  
    dyalog = os.fspath(brand_dir / 'dyalog.svg')
  
    gg = os.fspath(brand_dir / 'gg.svg')
  
    google_wallet = os.fspath(brand_dir / 'google-wallet.svg')
  
    cmplid = os.fspath(brand_dir / 'cmplid.svg')
  
    wikipedia_w = os.fspath(brand_dir / 'wikipedia-w.svg')
  
    deviantart = os.fspath(brand_dir / 'deviantart.svg')
  
    alipay = os.fspath(brand_dir / 'alipay.svg')
  
    ioxhost = os.fspath(brand_dir / 'ioxhost.svg')
  
    umbraco = os.fspath(brand_dir / 'umbraco.svg')
  
    dropbox = os.fspath(brand_dir / 'dropbox.svg')
  
    first_order_alt = os.fspath(brand_dir / 'first-order-alt.svg')
  
    algolia = os.fspath(brand_dir / 'algolia.svg')
  
    steam = os.fspath(brand_dir / 'steam.svg')
  
    neos = os.fspath(brand_dir / 'neos.svg')
  
    itch_io = os.fspath(brand_dir / 'itch-io.svg')
  
    git_alt = os.fspath(brand_dir / 'git-alt.svg')
  
    ups = os.fspath(brand_dir / 'ups.svg')
  
    hornbill = os.fspath(brand_dir / 'hornbill.svg')
  
    android = os.fspath(brand_dir / 'android.svg')
  
    stumbleupon = os.fspath(brand_dir / 'stumbleupon.svg')
  
    superpowers = os.fspath(brand_dir / 'superpowers.svg')
  
    bilibili = os.fspath(brand_dir / 'bilibili.svg')
  
    mdb = os.fspath(brand_dir / 'mdb.svg')
  
    yandex_international = os.fspath(brand_dir / 'yandex-international.svg')
  
    gripfire = os.fspath(brand_dir / 'gripfire.svg')
  
    erlang = os.fspath(brand_dir / 'erlang.svg')
  
    square_odnoklassniki = os.fspath(brand_dir / 'square-odnoklassniki.svg')
  
    hire_a_helper = os.fspath(brand_dir / 'hire-a-helper.svg')
  
    instagram = os.fspath(brand_dir / 'instagram.svg')
  
    shirtsinbulk = os.fspath(brand_dir / 'shirtsinbulk.svg')
  
    d_and_d_beyond = os.fspath(brand_dir / 'd-and-d-beyond.svg')
  
    octopus_deploy = os.fspath(brand_dir / 'octopus-deploy.svg')
  
    creative_commons_sampling = os.fspath(brand_dir / 'creative-commons-sampling.svg')
  
    expeditedssl = os.fspath(brand_dir / 'expeditedssl.svg')
  
    wpressr = os.fspath(brand_dir / 'wpressr.svg')
  
    mandalorian = os.fspath(brand_dir / 'mandalorian.svg')
  
    confluence = os.fspath(brand_dir / 'confluence.svg')
  
    deezer = os.fspath(brand_dir / 'deezer.svg')
  
    phoenix_squadron = os.fspath(brand_dir / 'phoenix-squadron.svg')
  
    linkedin_in = os.fspath(brand_dir / 'linkedin-in.svg')
  
    css3 = os.fspath(brand_dir / 'css3.svg')
  
    themeco = os.fspath(brand_dir / 'themeco.svg')
  
    critical_role = os.fspath(brand_dir / 'critical-role.svg')
  
    odnoklassniki = os.fspath(brand_dir / 'odnoklassniki.svg')
  
    etsy = os.fspath(brand_dir / 'etsy.svg')
  
    ebay = os.fspath(brand_dir / 'ebay.svg')
  
    blogger_b = os.fspath(brand_dir / 'blogger-b.svg')
  
    hive = os.fspath(brand_dir / 'hive.svg')
  
    leanpub = os.fspath(brand_dir / 'leanpub.svg')
  
    chrome = os.fspath(brand_dir / 'chrome.svg')
  
    jsfiddle = os.fspath(brand_dir / 'jsfiddle.svg')
  
    behance = os.fspath(brand_dir / 'behance.svg')
  
    square_lastfm = os.fspath(brand_dir / 'square-lastfm.svg')
  
    r_project = os.fspath(brand_dir / 'r-project.svg')
  
    ideal = os.fspath(brand_dir / 'ideal.svg')
  
    usps = os.fspath(brand_dir / 'usps.svg')
  
    weibo = os.fspath(brand_dir / 'weibo.svg')
  
    tiktok = os.fspath(brand_dir / 'tiktok.svg')
  
    reddit_alien = os.fspath(brand_dir / 'reddit-alien.svg')
  
    bitcoin = os.fspath(brand_dir / 'bitcoin.svg')
  
    ethereum = os.fspath(brand_dir / 'ethereum.svg')
  
    whatsapp = os.fspath(brand_dir / 'whatsapp.svg')
  
    digg = os.fspath(brand_dir / 'digg.svg')
  
    simplybuilt = os.fspath(brand_dir / 'simplybuilt.svg')
  
    red_river = os.fspath(brand_dir / 'red-river.svg')
  
    audible = os.fspath(brand_dir / 'audible.svg')
  
    rev = os.fspath(brand_dir / 'rev.svg')
  
    gitlab = os.fspath(brand_dir / 'gitlab.svg')
  
    opera = os.fspath(brand_dir / 'opera.svg')
  
    wodu = os.fspath(brand_dir / 'wodu.svg')
  
    cloudversify = os.fspath(brand_dir / 'cloudversify.svg')
  
    goodreads = os.fspath(brand_dir / 'goodreads.svg')
  
    waze = os.fspath(brand_dir / 'waze.svg')
  
    telegram = os.fspath(brand_dir / 'telegram.svg')
  
    square_steam = os.fspath(brand_dir / 'square-steam.svg')
  
    product_hunt = os.fspath(brand_dir / 'product-hunt.svg')
  
    megaport = os.fspath(brand_dir / 'megaport.svg')
  
    trello = os.fspath(brand_dir / 'trello.svg')
  
    dochub = os.fspath(brand_dir / 'dochub.svg')
  
    font_awesome = os.fspath(brand_dir / 'font-awesome.svg')
  
    square_snapchat = os.fspath(brand_dir / 'square-snapchat.svg')
  
    cc_mastercard = os.fspath(brand_dir / 'cc-mastercard.svg')
  
    firefox_browser = os.fspath(brand_dir / 'firefox-browser.svg')
  
    galactic_republic = os.fspath(brand_dir / 'galactic-republic.svg')
  
    joomla = os.fspath(brand_dir / 'joomla.svg')
  
    adversal = os.fspath(brand_dir / 'adversal.svg')
  
    accusoft = os.fspath(brand_dir / 'accusoft.svg')
  
    fedex = os.fspath(brand_dir / 'fedex.svg')
  
    square_x_twitter = os.fspath(brand_dir / 'square-x-twitter.svg')
  
    ussunnah = os.fspath(brand_dir / 'ussunnah.svg')
  
    cloudflare = os.fspath(brand_dir / 'cloudflare.svg')
  
    square_tumblr = os.fspath(brand_dir / 'square-tumblr.svg')
  
    golang = os.fspath(brand_dir / 'golang.svg')
  
    amazon = os.fspath(brand_dir / 'amazon.svg')
  
    hips = os.fspath(brand_dir / 'hips.svg')
  
    mixcloud = os.fspath(brand_dir / 'mixcloud.svg')
  
    square_threads = os.fspath(brand_dir / 'square-threads.svg')
  
    viacoin = os.fspath(brand_dir / 'viacoin.svg')
  
    itunes = os.fspath(brand_dir / 'itunes.svg')
  
    dribbble = os.fspath(brand_dir / 'dribbble.svg')
  
    node = os.fspath(brand_dir / 'node.svg')
  
    jenkins = os.fspath(brand_dir / 'jenkins.svg')
  
    lastfm = os.fspath(brand_dir / 'lastfm.svg')
  
    modx = os.fspath(brand_dir / 'modx.svg')
  
    magento = os.fspath(brand_dir / 'magento.svg')
  
    cuttlefish = os.fspath(brand_dir / 'cuttlefish.svg')
  
    teamspeak = os.fspath(brand_dir / 'teamspeak.svg')
  
    square_youtube = os.fspath(brand_dir / 'square-youtube.svg')
  
    pagelines = os.fspath(brand_dir / 'pagelines.svg')
  
    keycdn = os.fspath(brand_dir / 'keycdn.svg')
  
    bluetooth_b = os.fspath(brand_dir / 'bluetooth-b.svg')
  
    quinscape = os.fspath(brand_dir / 'quinscape.svg')
  
    cc_visa = os.fspath(brand_dir / 'cc-visa.svg')
  


class _Regular(Enum):
  
    face_laugh_beam = os.fspath(regular_dir / 'face-laugh-beam.svg')
  
    calendar_minus = os.fspath(regular_dir / 'calendar-minus.svg')
  
    file_audio = os.fspath(regular_dir / 'file-audio.svg')
  
    eye = os.fspath(regular_dir / 'eye.svg')
  
    hand_point_up = os.fspath(regular_dir / 'hand-point-up.svg')
  
    gem = os.fspath(regular_dir / 'gem.svg')
  
    keyboard = os.fspath(regular_dir / 'keyboard.svg')
  
    credit_card = os.fspath(regular_dir / 'credit-card.svg')
  
    lightbulb = os.fspath(regular_dir / 'lightbulb.svg')
  
    face_dizzy = os.fspath(regular_dir / 'face-dizzy.svg')
  
    moon = os.fspath(regular_dir / 'moon.svg')
  
    face_grin = os.fspath(regular_dir / 'face-grin.svg')
  
    face_laugh = os.fspath(regular_dir / 'face-laugh.svg')
  
    face_laugh_squint = os.fspath(regular_dir / 'face-laugh-squint.svg')
  
    square_full = os.fspath(regular_dir / 'square-full.svg')
  
    rectangle_xmark = os.fspath(regular_dir / 'rectangle-xmark.svg')
  
    face_grin_beam = os.fspath(regular_dir / 'face-grin-beam.svg')
  
    face_grin_stars = os.fspath(regular_dir / 'face-grin-stars.svg')
  
    face_laugh_wink = os.fspath(regular_dir / 'face-laugh-wink.svg')
  
    square_caret_right = os.fspath(regular_dir / 'square-caret-right.svg')
  
    face_grin_tears = os.fspath(regular_dir / 'face-grin-tears.svg')
  
    money_bill_1 = os.fspath(regular_dir / 'money-bill-1.svg')
  
    face_grin_squint = os.fspath(regular_dir / 'face-grin-squint.svg')
  
    face_rolling_eyes = os.fspath(regular_dir / 'face-rolling-eyes.svg')
  
    circle_stop = os.fspath(regular_dir / 'circle-stop.svg')
  
    share_from_square = os.fspath(regular_dir / 'share-from-square.svg')
  
    thumbs_up = os.fspath(regular_dir / 'thumbs-up.svg')
  
    face_smile_beam = os.fspath(regular_dir / 'face-smile-beam.svg')
  
    face_grin_tongue_wink = os.fspath(regular_dir / 'face-grin-tongue-wink.svg')
  
    chess_queen = os.fspath(regular_dir / 'chess-queen.svg')
  
    face_angry = os.fspath(regular_dir / 'face-angry.svg')
  
    calendar_xmark = os.fspath(regular_dir / 'calendar-xmark.svg')
  
    window_maximize = os.fspath(regular_dir / 'window-maximize.svg')
  
    id_card = os.fspath(regular_dir / 'id-card.svg')
  
    bell_slash = os.fspath(regular_dir / 'bell-slash.svg')
  
    circle_dot = os.fspath(regular_dir / 'circle-dot.svg')
  
    file_video = os.fspath(regular_dir / 'file-video.svg')
  
    hourglass_half = os.fspath(regular_dir / 'hourglass-half.svg')
  
    chess_rook = os.fspath(regular_dir / 'chess-rook.svg')
  
    file_zipper = os.fspath(regular_dir / 'file-zipper.svg')
  
    comments = os.fspath(regular_dir / 'comments.svg')
  
    face_grimace = os.fspath(regular_dir / 'face-grimace.svg')
  
    circle_left = os.fspath(regular_dir / 'circle-left.svg')
  
    eye_slash = os.fspath(regular_dir / 'eye-slash.svg')
  
    circle_play = os.fspath(regular_dir / 'circle-play.svg')
  
    hand_peace = os.fspath(regular_dir / 'hand-peace.svg')
  
    circle_up = os.fspath(regular_dir / 'circle-up.svg')
  
    hand_pointer = os.fspath(regular_dir / 'hand-pointer.svg')
  
    copyright = os.fspath(regular_dir / 'copyright.svg')
  
    calendar_plus = os.fspath(regular_dir / 'calendar-plus.svg')
  
    life_ring = os.fspath(regular_dir / 'life-ring.svg')
  
    file_pdf = os.fspath(regular_dir / 'file-pdf.svg')
  
    hand_scissors = os.fspath(regular_dir / 'hand-scissors.svg')
  
    hard_drive = os.fspath(regular_dir / 'hard-drive.svg')
  
    circle_user = os.fspath(regular_dir / 'circle-user.svg')
  
    chess_king = os.fspath(regular_dir / 'chess-king.svg')
  
    face_kiss_wink_heart = os.fspath(regular_dir / 'face-kiss-wink-heart.svg')
  
    hand_point_left = os.fspath(regular_dir / 'hand-point-left.svg')
  
    circle_down = os.fspath(regular_dir / 'circle-down.svg')
  
    clock = os.fspath(regular_dir / 'clock.svg')
  
    folder = os.fspath(regular_dir / 'folder.svg')
  
    window_restore = os.fspath(regular_dir / 'window-restore.svg')
  
    bookmark = os.fspath(regular_dir / 'bookmark.svg')
  
    chess_pawn = os.fspath(regular_dir / 'chess-pawn.svg')
  
    circle_check = os.fspath(regular_dir / 'circle-check.svg')
  
    clone = os.fspath(regular_dir / 'clone.svg')
  
    envelope_open = os.fspath(regular_dir / 'envelope-open.svg')
  
    address_book = os.fspath(regular_dir / 'address-book.svg')
  
    face_grin_hearts = os.fspath(regular_dir / 'face-grin-hearts.svg')
  
    square_plus = os.fspath(regular_dir / 'square-plus.svg')
  
    hospital = os.fspath(regular_dir / 'hospital.svg')
  
    floppy_disk = os.fspath(regular_dir / 'floppy-disk.svg')
  
    file_word = os.fspath(regular_dir / 'file-word.svg')
  
    star_half = os.fspath(regular_dir / 'star-half.svg')
  
    newspaper = os.fspath(regular_dir / 'newspaper.svg')
  
    calendar_check = os.fspath(regular_dir / 'calendar-check.svg')
  
    comment_dots = os.fspath(regular_dir / 'comment-dots.svg')
  
    sun = os.fspath(regular_dir / 'sun.svg')
  
    circle_right = os.fspath(regular_dir / 'circle-right.svg')
  
    envelope = os.fspath(regular_dir / 'envelope.svg')
  
    paste = os.fspath(regular_dir / 'paste.svg')
  
    face_smile_wink = os.fspath(regular_dir / 'face-smile-wink.svg')
  
    clipboard = os.fspath(regular_dir / 'clipboard.svg')
  
    square_minus = os.fspath(regular_dir / 'square-minus.svg')
  
    star = os.fspath(regular_dir / 'star.svg')
  
    circle_pause = os.fspath(regular_dir / 'circle-pause.svg')
  
    square = os.fspath(regular_dir / 'square.svg')
  
    flag = os.fspath(regular_dir / 'flag.svg')
  
    face_kiss_beam = os.fspath(regular_dir / 'face-kiss-beam.svg')
  
    address_card = os.fspath(regular_dir / 'address-card.svg')
  
    id_badge = os.fspath(regular_dir / 'id-badge.svg')
  
    user = os.fspath(regular_dir / 'user.svg')
  
    hourglass = os.fspath(regular_dir / 'hourglass.svg')
  
    handshake = os.fspath(regular_dir / 'handshake.svg')
  
    calendar_days = os.fspath(regular_dir / 'calendar-days.svg')
  
    face_grin_tongue = os.fspath(regular_dir / 'face-grin-tongue.svg')
  
    window_minimize = os.fspath(regular_dir / 'window-minimize.svg')
  
    thumbs_down = os.fspath(regular_dir / 'thumbs-down.svg')
  
    note_sticky = os.fspath(regular_dir / 'note-sticky.svg')
  
    file_excel = os.fspath(regular_dir / 'file-excel.svg')
  
    face_grin_tongue_squint = os.fspath(regular_dir / 'face-grin-tongue-squint.svg')
  
    file_powerpoint = os.fspath(regular_dir / 'file-powerpoint.svg')
  
    paper_plane = os.fspath(regular_dir / 'paper-plane.svg')
  
    face_meh = os.fspath(regular_dir / 'face-meh.svg')
  
    pen_to_square = os.fspath(regular_dir / 'pen-to-square.svg')
  
    face_sad_tear = os.fspath(regular_dir / 'face-sad-tear.svg')
  
    square_caret_down = os.fspath(regular_dir / 'square-caret-down.svg')
  
    trash_can = os.fspath(regular_dir / 'trash-can.svg')
  
    hand = os.fspath(regular_dir / 'hand.svg')
  
    face_tired = os.fspath(regular_dir / 'face-tired.svg')
  
    face_grin_wide = os.fspath(regular_dir / 'face-grin-wide.svg')
  
    copy = os.fspath(regular_dir / 'copy.svg')
  
    calendar = os.fspath(regular_dir / 'calendar.svg')
  
    face_flushed = os.fspath(regular_dir / 'face-flushed.svg')
  
    circle_xmark = os.fspath(regular_dir / 'circle-xmark.svg')
  
    face_smile = os.fspath(regular_dir / 'face-smile.svg')
  
    chess_bishop = os.fspath(regular_dir / 'chess-bishop.svg')
  
    star_half_stroke = os.fspath(regular_dir / 'star-half-stroke.svg')
  
    face_grin_wink = os.fspath(regular_dir / 'face-grin-wink.svg')
  
    face_sad_cry = os.fspath(regular_dir / 'face-sad-cry.svg')
  
    file_lines = os.fspath(regular_dir / 'file-lines.svg')
  
    face_grin_squint_tears = os.fspath(regular_dir / 'face-grin-squint-tears.svg')
  
    hand_point_right = os.fspath(regular_dir / 'hand-point-right.svg')
  
    face_frown_open = os.fspath(regular_dir / 'face-frown-open.svg')
  
    image = os.fspath(regular_dir / 'image.svg')
  
    folder_open = os.fspath(regular_dir / 'folder-open.svg')
  
    folder_closed = os.fspath(regular_dir / 'folder-closed.svg')
  
    building = os.fspath(regular_dir / 'building.svg')
  
    message = os.fspath(regular_dir / 'message.svg')
  
    face_kiss = os.fspath(regular_dir / 'face-kiss.svg')
  
    object_ungroup = os.fspath(regular_dir / 'object-ungroup.svg')
  
    square_caret_left = os.fspath(regular_dir / 'square-caret-left.svg')
  
    square_caret_up = os.fspath(regular_dir / 'square-caret-up.svg')
  
    hand_lizard = os.fspath(regular_dir / 'hand-lizard.svg')
  
    face_meh_blank = os.fspath(regular_dir / 'face-meh-blank.svg')
  
    file = os.fspath(regular_dir / 'file.svg')
  
    comment = os.fspath(regular_dir / 'comment.svg')
  
    bell = os.fspath(regular_dir / 'bell.svg')
  
    compass = os.fspath(regular_dir / 'compass.svg')
  
    circle = os.fspath(regular_dir / 'circle.svg')
  
    futbol = os.fspath(regular_dir / 'futbol.svg')
  
    square_check = os.fspath(regular_dir / 'square-check.svg')
  
    face_surprise = os.fspath(regular_dir / 'face-surprise.svg')
  
    snowflake = os.fspath(regular_dir / 'snowflake.svg')
  
    face_grin_beam_sweat = os.fspath(regular_dir / 'face-grin-beam-sweat.svg')
  
    images = os.fspath(regular_dir / 'images.svg')
  
    circle_question = os.fspath(regular_dir / 'circle-question.svg')
  
    face_frown = os.fspath(regular_dir / 'face-frown.svg')
  
    file_image = os.fspath(regular_dir / 'file-image.svg')
  
    map = os.fspath(regular_dir / 'map.svg')
  
    closed_captioning = os.fspath(regular_dir / 'closed-captioning.svg')
  
    font_awesome = os.fspath(regular_dir / 'font-awesome.svg')
  
    hand_back_fist = os.fspath(regular_dir / 'hand-back-fist.svg')
  
    registered = os.fspath(regular_dir / 'registered.svg')
  
    chart_bar = os.fspath(regular_dir / 'chart-bar.svg')
  
    file_code = os.fspath(regular_dir / 'file-code.svg')
  
    lemon = os.fspath(regular_dir / 'lemon.svg')
  
    chess_knight = os.fspath(regular_dir / 'chess-knight.svg')
  
    rectangle_list = os.fspath(regular_dir / 'rectangle-list.svg')
  
    object_group = os.fspath(regular_dir / 'object-group.svg')
  
    hand_point_down = os.fspath(regular_dir / 'hand-point-down.svg')
  
    heart = os.fspath(regular_dir / 'heart.svg')
  
    hand_spock = os.fspath(regular_dir / 'hand-spock.svg')
  


class _Solid(Enum):
  
    p = os.fspath(solid_dir / 'p.svg')
  
    mercury = os.fspath(solid_dir / 'mercury.svg')
  
    circle_exclamation = os.fspath(solid_dir / 'circle-exclamation.svg')
  
    face_laugh_beam = os.fspath(solid_dir / 'face-laugh-beam.svg')
  
    rotate_right = os.fspath(solid_dir / 'rotate-right.svg')
  
    calendar_minus = os.fspath(solid_dir / 'calendar-minus.svg')
  
    user_astronaut = os.fspath(solid_dir / 'user-astronaut.svg')
  
    file_audio = os.fspath(solid_dir / 'file-audio.svg')
  
    eye = os.fspath(solid_dir / 'eye.svg')
  
    plug_circle_check = os.fspath(solid_dir / 'plug-circle-check.svg')
  
    arrows_up_down_left_right = os.fspath(solid_dir / 'arrows-up-down-left-right.svg')
  
    hand_point_up = os.fspath(solid_dir / 'hand-point-up.svg')
  
    computer_mouse = os.fspath(solid_dir / 'computer-mouse.svg')
  
    satellite = os.fspath(solid_dir / 'satellite.svg')
  
    gem = os.fspath(solid_dir / 'gem.svg')
  
    arrow_up_wide_short = os.fspath(solid_dir / 'arrow-up-wide-short.svg')
  
    bolt = os.fspath(solid_dir / 'bolt.svg')
  
    square_person_confined = os.fspath(solid_dir / 'square-person-confined.svg')
  
    file_prescription = os.fspath(solid_dir / 'file-prescription.svg')
  
    person_arrow_down_to_line = os.fspath(solid_dir / 'person-arrow-down-to-line.svg')
  
    reply_all = os.fspath(solid_dir / 'reply-all.svg')
  
    dice_four = os.fspath(solid_dir / 'dice-four.svg')
  
    house_laptop = os.fspath(solid_dir / 'house-laptop.svg')
  
    align_left = os.fspath(solid_dir / 'align-left.svg')
  
    x = os.fspath(solid_dir / 'x.svg')
  
    arrows_left_right_to_line = os.fspath(solid_dir / 'arrows-left-right-to-line.svg')
  
    whiskey_glass = os.fspath(solid_dir / 'whiskey-glass.svg')
  
    dice_five = os.fspath(solid_dir / 'dice-five.svg')
  
    ethernet = os.fspath(solid_dir / 'ethernet.svg')
  
    k = os.fspath(solid_dir / 'k.svg')
  
    tower_broadcast = os.fspath(solid_dir / 'tower-broadcast.svg')
  
    road_lock = os.fspath(solid_dir / 'road-lock.svg')
  
    table_list = os.fspath(solid_dir / 'table-list.svg')
  
    building_ngo = os.fspath(solid_dir / 'building-ngo.svg')
  
    dragon = os.fspath(solid_dir / 'dragon.svg')
  
    industry = os.fspath(solid_dir / 'industry.svg')
  
    magnifying_glass = os.fspath(solid_dir / 'magnifying-glass.svg')
  
    person_snowboarding = os.fspath(solid_dir / 'person-snowboarding.svg')
  
    up_down_left_right = os.fspath(solid_dir / 'up-down-left-right.svg')
  
    arrow_up_right_from_square = os.fspath(solid_dir / 'arrow-up-right-from-square.svg')
  
    file_circle_minus = os.fspath(solid_dir / 'file-circle-minus.svg')
  
    temperature_full = os.fspath(solid_dir / 'temperature-full.svg')
  
    arrow_right_from_bracket = os.fspath(solid_dir / 'arrow-right-from-bracket.svg')
  
    litecoin_sign = os.fspath(solid_dir / 'litecoin-sign.svg')
  
    grip_lines = os.fspath(solid_dir / 'grip-lines.svg')
  
    building_circle_arrow_right = os.fspath(solid_dir / 'building-circle-arrow-right.svg')
  
    list_ol = os.fspath(solid_dir / 'list-ol.svg')
  
    signal = os.fspath(solid_dir / 'signal.svg')
  
    caret_up = os.fspath(solid_dir / 'caret-up.svg')
  
    battery_empty = os.fspath(solid_dir / 'battery-empty.svg')
  
    anchor = os.fspath(solid_dir / 'anchor.svg')
  
    bullseye = os.fspath(solid_dir / 'bullseye.svg')
  
    person = os.fspath(solid_dir / 'person.svg')
  
    keyboard = os.fspath(solid_dir / 'keyboard.svg')
  
    check = os.fspath(solid_dir / 'check.svg')
  
    bridge_circle_exclamation = os.fspath(solid_dir / 'bridge-circle-exclamation.svg')
  
    chess = os.fspath(solid_dir / 'chess.svg')
  
    laptop_file = os.fspath(solid_dir / 'laptop-file.svg')
  
    joint = os.fspath(solid_dir / 'joint.svg')
  
    person_through_window = os.fspath(solid_dir / 'person-through-window.svg')
  
    radio = os.fspath(solid_dir / 'radio.svg')
  
    i_cursor = os.fspath(solid_dir / 'i-cursor.svg')
  
    align_justify = os.fspath(solid_dir / 'align-justify.svg')
  
    landmark_dome = os.fspath(solid_dir / 'landmark-dome.svg')
  
    warehouse = os.fspath(solid_dir / 'warehouse.svg')
  
    guitar = os.fspath(solid_dir / 'guitar.svg')
  
    book_atlas = os.fspath(solid_dir / 'book-atlas.svg')
  
    credit_card = os.fspath(solid_dir / 'credit-card.svg')
  
    bars_progress = os.fspath(solid_dir / 'bars-progress.svg')
  
    square_poll_vertical = os.fspath(solid_dir / 'square-poll-vertical.svg')
  
    lightbulb = os.fspath(solid_dir / 'lightbulb.svg')
  
    sort_down = os.fspath(solid_dir / 'sort-down.svg')
  
    spa = os.fspath(solid_dir / 'spa.svg')
  
    face_dizzy = os.fspath(solid_dir / 'face-dizzy.svg')
  
    atom = os.fspath(solid_dir / 'atom.svg')
  
    person_breastfeeding = os.fspath(solid_dir / 'person-breastfeeding.svg')
  
    bezier_curve = os.fspath(solid_dir / 'bezier-curve.svg')
  
    compress = os.fspath(solid_dir / 'compress.svg')
  
    mosquito_net = os.fspath(solid_dir / 'mosquito-net.svg')
  
    head_side_mask = os.fspath(solid_dir / 'head-side-mask.svg')
  
    viruses = os.fspath(solid_dir / 'viruses.svg')
  
    plane_circle_check = os.fspath(solid_dir / 'plane-circle-check.svg')
  
    quote_right = os.fspath(solid_dir / 'quote-right.svg')
  
    gauge = os.fspath(solid_dir / 'gauge.svg')
  
    business_time = os.fspath(solid_dir / 'business-time.svg')
  
    tags = os.fspath(solid_dir / 'tags.svg')
  
    moon = os.fspath(solid_dir / 'moon.svg')
  
    percent = os.fspath(solid_dir / 'percent.svg')
  
    plug_circle_plus = os.fspath(solid_dir / 'plug-circle-plus.svg')
  
    earth_oceania = os.fspath(solid_dir / 'earth-oceania.svg')
  
    money_bill_wheat = os.fspath(solid_dir / 'money-bill-wheat.svg')
  
    text_height = os.fspath(solid_dir / 'text-height.svg')
  
    house_chimney_crack = os.fspath(solid_dir / 'house-chimney-crack.svg')
  
    neuter = os.fspath(solid_dir / 'neuter.svg')
  
    land_mine_on = os.fspath(solid_dir / 'land-mine-on.svg')
  
    face_grin = os.fspath(solid_dir / 'face-grin.svg')
  
    file_pen = os.fspath(solid_dir / 'file-pen.svg')
  
    arrow_up_from_bracket = os.fspath(solid_dir / 'arrow-up-from-bracket.svg')
  
    baht_sign = os.fspath(solid_dir / 'baht-sign.svg')
  
    eye_dropper = os.fspath(solid_dir / 'eye-dropper.svg')
  
    dice_two = os.fspath(solid_dir / 'dice-two.svg')
  
    comment_sms = os.fspath(solid_dir / 'comment-sms.svg')
  
    draw_polygon = os.fspath(solid_dir / 'draw-polygon.svg')
  
    unlock_keyhole = os.fspath(solid_dir / 'unlock-keyhole.svg')
  
    question = os.fspath(solid_dir / 'question.svg')
  
    ring = os.fspath(solid_dir / 'ring.svg')
  
    slash = os.fspath(solid_dir / 'slash.svg')
  
    socks = os.fspath(solid_dir / 'socks.svg')
  
    football = os.fspath(solid_dir / 'football.svg')
  
    ferry = os.fspath(solid_dir / 'ferry.svg')
  
    mars_and_venus_burst = os.fspath(solid_dir / 'mars-and-venus-burst.svg')
  
    folder_plus = os.fspath(solid_dir / 'folder-plus.svg')
  
    truck_plane = os.fspath(solid_dir / 'truck-plane.svg')
  
    inbox = os.fspath(solid_dir / 'inbox.svg')
  
    drumstick_bite = os.fspath(solid_dir / 'drumstick-bite.svg')
  
    face_laugh = os.fspath(solid_dir / 'face-laugh.svg')
  
    fingerprint = os.fspath(solid_dir / 'fingerprint.svg')
  
    fire = os.fspath(solid_dir / 'fire.svg')
  
    arrow_right_long = os.fspath(solid_dir / 'arrow-right-long.svg')
  
    circle_half_stroke = os.fspath(solid_dir / 'circle-half-stroke.svg')
  
    face_laugh_squint = os.fspath(solid_dir / 'face-laugh-squint.svg')
  
    frog = os.fspath(solid_dir / 'frog.svg')
  
    arrow_left_long = os.fspath(solid_dir / 'arrow-left-long.svg')
  
    font = os.fspath(solid_dir / 'font.svg')
  
    campground = os.fspath(solid_dir / 'campground.svg')
  
    gear = os.fspath(solid_dir / 'gear.svg')
  
    angle_down = os.fspath(solid_dir / 'angle-down.svg')
  
    comment_medical = os.fspath(solid_dir / 'comment-medical.svg')
  
    poop = os.fspath(solid_dir / 'poop.svg')
  
    plant_wilt = os.fspath(solid_dir / 'plant-wilt.svg')
  
    anchor_lock = os.fspath(solid_dir / 'anchor-lock.svg')
  
    box_open = os.fspath(solid_dir / 'box-open.svg')
  
    shop_lock = os.fspath(solid_dir / 'shop-lock.svg')
  
    pump_soap = os.fspath(solid_dir / 'pump-soap.svg')
  
    phone = os.fspath(solid_dir / 'phone.svg')
  
    angle_up = os.fspath(solid_dir / 'angle-up.svg')
  
    diamond = os.fspath(solid_dir / 'diamond.svg')
  
    user_minus = os.fspath(solid_dir / 'user-minus.svg')
  
    square_full = os.fspath(solid_dir / 'square-full.svg')
  
    money_bill_trend_up = os.fspath(solid_dir / 'money-bill-trend-up.svg')
  
    rectangle_xmark = os.fspath(solid_dir / 'rectangle-xmark.svg')
  
    clipboard_user = os.fspath(solid_dir / 'clipboard-user.svg')
  
    house_crack = os.fspath(solid_dir / 'house-crack.svg')
  
    truck_medical = os.fspath(solid_dir / 'truck-medical.svg')
  
    helicopter_symbol = os.fspath(solid_dir / 'helicopter-symbol.svg')
  
    file_import = os.fspath(solid_dir / 'file-import.svg')
  
    dumpster_fire = os.fspath(solid_dir / 'dumpster-fire.svg')
  
    phone_flip = os.fspath(solid_dir / 'phone-flip.svg')
  
    chart_simple = os.fspath(solid_dir / 'chart-simple.svg')
  
    helicopter = os.fspath(solid_dir / 'helicopter.svg')
  
    table = os.fspath(solid_dir / 'table.svg')
  
    arrow_down_long = os.fspath(solid_dir / 'arrow-down-long.svg')
  
    igloo = os.fspath(solid_dir / 'igloo.svg')
  
    arrows_split_up_and_left = os.fspath(solid_dir / 'arrows-split-up-and-left.svg')
  
    hippo = os.fspath(solid_dir / 'hippo.svg')
  
    arrow_left = os.fspath(solid_dir / 'arrow-left.svg')
  
    money_bill_1_wave = os.fspath(solid_dir / 'money-bill-1-wave.svg')
  
    right_from_bracket = os.fspath(solid_dir / 'right-from-bracket.svg')
  
    heading = os.fspath(solid_dir / 'heading.svg')
  
    arrow_pointer = os.fspath(solid_dir / 'arrow-pointer.svg')
  
    code_pull_request = os.fspath(solid_dir / 'code-pull-request.svg')
  
    chart_pie = os.fspath(solid_dir / 'chart-pie.svg')
  
    bowl_food = os.fspath(solid_dir / 'bowl-food.svg')
  
    pizza_slice = os.fspath(solid_dir / 'pizza-slice.svg')
  
    mars_stroke = os.fspath(solid_dir / 'mars-stroke.svg')
  
    less_than_equal = os.fspath(solid_dir / 'less-than-equal.svg')
  
    plug_circle_exclamation = os.fspath(solid_dir / 'plug-circle-exclamation.svg')
  
    square_h = os.fspath(solid_dir / 'square-h.svg')
  
    arrow_up_9_1 = os.fspath(solid_dir / 'arrow-up-9-1.svg')
  
    kitchen_set = os.fspath(solid_dir / 'kitchen-set.svg')
  
    user_secret = os.fspath(solid_dir / 'user-secret.svg')
  
    scale_unbalanced = os.fspath(solid_dir / 'scale-unbalanced.svg')
  
    bomb = os.fspath(solid_dir / 'bomb.svg')
  
    face_grin_beam = os.fspath(solid_dir / 'face-grin-beam.svg')
  
    fire_flame_curved = os.fspath(solid_dir / 'fire-flame-curved.svg')
  
    person_walking_luggage = os.fspath(solid_dir / 'person-walking-luggage.svg')
  
    laptop = os.fspath(solid_dir / 'laptop.svg')
  
    person_falling_burst = os.fspath(solid_dir / 'person-falling-burst.svg')
  
    face_grin_stars = os.fspath(solid_dir / 'face-grin-stars.svg')
  
    arrows_spin = os.fspath(solid_dir / 'arrows-spin.svg')
  
    table_tennis_paddle_ball = os.fspath(solid_dir / 'table-tennis-paddle-ball.svg')
  
    arrow_down_short_wide = os.fspath(solid_dir / 'arrow-down-short-wide.svg')
  
    child_dress = os.fspath(solid_dir / 'child-dress.svg')
  
    money_check_dollar = os.fspath(solid_dir / 'money-check-dollar.svg')
  
    _1 = os.fspath(solid_dir / '1.svg')
  
    temperature_arrow_up = os.fspath(solid_dir / 'temperature-arrow-up.svg')
  
    qrcode = os.fspath(solid_dir / 'qrcode.svg')
  
    plug_circle_xmark = os.fspath(solid_dir / 'plug-circle-xmark.svg')
  
    tents = os.fspath(solid_dir / 'tents.svg')
  
    code_commit = os.fspath(solid_dir / 'code-commit.svg')
  
    minus = os.fspath(solid_dir / 'minus.svg')
  
    face_laugh_wink = os.fspath(solid_dir / 'face-laugh-wink.svg')
  
    cookie = os.fspath(solid_dir / 'cookie.svg')
  
    square_caret_right = os.fspath(solid_dir / 'square-caret-right.svg')
  
    door_open = os.fspath(solid_dir / 'door-open.svg')
  
    heart_circle_xmark = os.fspath(solid_dir / 'heart-circle-xmark.svg')
  
    toilet_paper = os.fspath(solid_dir / 'toilet-paper.svg')
  
    table_cells = os.fspath(solid_dir / 'table-cells.svg')
  
    angles_left = os.fspath(solid_dir / 'angles-left.svg')
  
    plane_circle_exclamation = os.fspath(solid_dir / 'plane-circle-exclamation.svg')
  
    person_circle_question = os.fspath(solid_dir / 'person-circle-question.svg')
  
    gears = os.fspath(solid_dir / 'gears.svg')
  
    stopwatch_20 = os.fspath(solid_dir / 'stopwatch-20.svg')
  
    basketball = os.fspath(solid_dir / 'basketball.svg')
  
    box_archive = os.fspath(solid_dir / 'box-archive.svg')
  
    parachute_box = os.fspath(solid_dir / 'parachute-box.svg')
  
    truck_ramp_box = os.fspath(solid_dir / 'truck-ramp-box.svg')
  
    train_tram = os.fspath(solid_dir / 'train-tram.svg')
  
    face_grin_tears = os.fspath(solid_dir / 'face-grin-tears.svg')
  
    user_check = os.fspath(solid_dir / 'user-check.svg')
  
    skull = os.fspath(solid_dir / 'skull.svg')
  
    money_bill_1 = os.fspath(solid_dir / 'money-bill-1.svg')
  
    hands_bound = os.fspath(solid_dir / 'hands-bound.svg')
  
    unlock = os.fspath(solid_dir / 'unlock.svg')
  
    euro_sign = os.fspath(solid_dir / 'euro-sign.svg')
  
    face_grin_squint = os.fspath(solid_dir / 'face-grin-squint.svg')
  
    ear_deaf = os.fspath(solid_dir / 'ear-deaf.svg')
  
    face_rolling_eyes = os.fspath(solid_dir / 'face-rolling-eyes.svg')
  
    person_dress = os.fspath(solid_dir / 'person-dress.svg')
  
    download = os.fspath(solid_dir / 'download.svg')
  
    jug_detergent = os.fspath(solid_dir / 'jug-detergent.svg')
  
    tractor = os.fspath(solid_dir / 'tractor.svg')
  
    icons = os.fspath(solid_dir / 'icons.svg')
  
    microphone = os.fspath(solid_dir / 'microphone.svg')
  
    faucet_drip = os.fspath(solid_dir / 'faucet-drip.svg')
  
    peso_sign = os.fspath(solid_dir / 'peso-sign.svg')
  
    circle_stop = os.fspath(solid_dir / 'circle-stop.svg')
  
    tv = os.fspath(solid_dir / 'tv.svg')
  
    share_from_square = os.fspath(solid_dir / 'share-from-square.svg')
  
    hanukiah = os.fspath(solid_dir / 'hanukiah.svg')
  
    book_open = os.fspath(solid_dir / 'book-open.svg')
  
    thumbs_up = os.fspath(solid_dir / 'thumbs-up.svg')
  
    plane_circle_xmark = os.fspath(solid_dir / 'plane-circle-xmark.svg')
  
    train_subway = os.fspath(solid_dir / 'train-subway.svg')
  
    house_signal = os.fspath(solid_dir / 'house-signal.svg')
  
    chalkboard_user = os.fspath(solid_dir / 'chalkboard-user.svg')
  
    network_wired = os.fspath(solid_dir / 'network-wired.svg')
  
    fire_burner = os.fspath(solid_dir / 'fire-burner.svg')
  
    dice_d20 = os.fspath(solid_dir / 'dice-d20.svg')
  
    truck_field_un = os.fspath(solid_dir / 'truck-field-un.svg')
  
    bacon = os.fspath(solid_dir / 'bacon.svg')
  
    plug = os.fspath(solid_dir / 'plug.svg')
  
    y = os.fspath(solid_dir / 'y.svg')
  
    stop = os.fspath(solid_dir / 'stop.svg')
  
    cloud_rain = os.fspath(solid_dir / 'cloud-rain.svg')
  
    heart_circle_bolt = os.fspath(solid_dir / 'heart-circle-bolt.svg')
  
    comments_dollar = os.fspath(solid_dir / 'comments-dollar.svg')
  
    spaghetti_monster_flying = os.fspath(solid_dir / 'spaghetti-monster-flying.svg')
  
    notes_medical = os.fspath(solid_dir / 'notes-medical.svg')
  
    user_large = os.fspath(solid_dir / 'user-large.svg')
  
    person_circle_xmark = os.fspath(solid_dir / 'person-circle-xmark.svg')
  
    person_cane = os.fspath(solid_dir / 'person-cane.svg')
  
    ship = os.fspath(solid_dir / 'ship.svg')
  
    toggle_on = os.fspath(solid_dir / 'toggle-on.svg')
  
    tent_arrow_down_to_line = os.fspath(solid_dir / 'tent-arrow-down-to-line.svg')
  
    user_lock = os.fspath(solid_dir / 'user-lock.svg')
  
    face_smile_beam = os.fspath(solid_dir / 'face-smile-beam.svg')
  
    backward = os.fspath(solid_dir / 'backward.svg')
  
    apple_whole = os.fspath(solid_dir / 'apple-whole.svg')
  
    snowman = os.fspath(solid_dir / 'snowman.svg')
  
    spray_can_sparkles = os.fspath(solid_dir / 'spray-can-sparkles.svg')
  
    hands_clapping = os.fspath(solid_dir / 'hands-clapping.svg')
  
    blender_phone = os.fspath(solid_dir / 'blender-phone.svg')
  
    bridge_water = os.fspath(solid_dir / 'bridge-water.svg')
  
    circle_notch = os.fspath(solid_dir / 'circle-notch.svg')
  
    sink = os.fspath(solid_dir / 'sink.svg')
  
    envelope_circle_check = os.fspath(solid_dir / 'envelope-circle-check.svg')
  
    face_grin_tongue_wink = os.fspath(solid_dir / 'face-grin-tongue-wink.svg')
  
    _9 = os.fspath(solid_dir / '9.svg')
  
    tooth = os.fspath(solid_dir / 'tooth.svg')
  
    pallet = os.fspath(solid_dir / 'pallet.svg')
  
    user_group = os.fspath(solid_dir / 'user-group.svg')
  
    microphone_lines = os.fspath(solid_dir / 'microphone-lines.svg')
  
    shrimp = os.fspath(solid_dir / 'shrimp.svg')
  
    otter = os.fspath(solid_dir / 'otter.svg')
  
    shapes = os.fspath(solid_dir / 'shapes.svg')
  
    tent = os.fspath(solid_dir / 'tent.svg')
  
    teeth = os.fspath(solid_dir / 'teeth.svg')
  
    cash_register = os.fspath(solid_dir / 'cash-register.svg')
  
    hand_holding = os.fspath(solid_dir / 'hand-holding.svg')
  
    person_burst = os.fspath(solid_dir / 'person-burst.svg')
  
    chess_queen = os.fspath(solid_dir / 'chess-queen.svg')
  
    face_angry = os.fspath(solid_dir / 'face-angry.svg')
  
    cloud_sun = os.fspath(solid_dir / 'cloud-sun.svg')
  
    paw = os.fspath(solid_dir / 'paw.svg')
  
    building_lock = os.fspath(solid_dir / 'building-lock.svg')
  
    mobile_button = os.fspath(solid_dir / 'mobile-button.svg')
  
    weight_scale = os.fspath(solid_dir / 'weight-scale.svg')
  
    ban_smoking = os.fspath(solid_dir / 'ban-smoking.svg')
  
    hill_rockslide = os.fspath(solid_dir / 'hill-rockslide.svg')
  
    xmark = os.fspath(solid_dir / 'xmark.svg')
  
    square_share_nodes = os.fspath(solid_dir / 'square-share-nodes.svg')
  
    up_long = os.fspath(solid_dir / 'up-long.svg')
  
    house_circle_exclamation = os.fspath(solid_dir / 'house-circle-exclamation.svg')
  
    diagram_next = os.fspath(solid_dir / 'diagram-next.svg')
  
    calendar_xmark = os.fspath(solid_dir / 'calendar-xmark.svg')
  
    people_group = os.fspath(solid_dir / 'people-group.svg')
  
    ban = os.fspath(solid_dir / 'ban.svg')
  
    vest = os.fspath(solid_dir / 'vest.svg')
  
    window_maximize = os.fspath(solid_dir / 'window-maximize.svg')
  
    cloud_moon = os.fspath(solid_dir / 'cloud-moon.svg')
  
    mound = os.fspath(solid_dir / 'mound.svg')
  
    braille = os.fspath(solid_dir / 'braille.svg')
  
    tablet_button = os.fspath(solid_dir / 'tablet-button.svg')
  
    id_card = os.fspath(solid_dir / 'id-card.svg')
  
    bell_slash = os.fspath(solid_dir / 'bell-slash.svg')
  
    martini_glass = os.fspath(solid_dir / 'martini-glass.svg')
  
    mask_face = os.fspath(solid_dir / 'mask-face.svg')
  
    people_roof = os.fspath(solid_dir / 'people-roof.svg')
  
    heart_circle_exclamation = os.fspath(solid_dir / 'heart-circle-exclamation.svg')
  
    comment_dollar = os.fspath(solid_dir / 'comment-dollar.svg')
  
    van_shuttle = os.fspath(solid_dir / 'van-shuttle.svg')
  
    calendar_week = os.fspath(solid_dir / 'calendar-week.svg')
  
    briefcase_medical = os.fspath(solid_dir / 'briefcase-medical.svg')
  
    democrat = os.fspath(solid_dir / 'democrat.svg')
  
    plane_departure = os.fspath(solid_dir / 'plane-departure.svg')
  
    worm = os.fspath(solid_dir / 'worm.svg')
  
    car_side = os.fspath(solid_dir / 'car-side.svg')
  
    shuffle = os.fspath(solid_dir / 'shuffle.svg')
  
    ruble_sign = os.fspath(solid_dir / 'ruble-sign.svg')
  
    person_booth = os.fspath(solid_dir / 'person-booth.svg')
  
    receipt = os.fspath(solid_dir / 'receipt.svg')
  
    ear_listen = os.fspath(solid_dir / 'ear-listen.svg')
  
    cart_flatbed = os.fspath(solid_dir / 'cart-flatbed.svg')
  
    users_rays = os.fspath(solid_dir / 'users-rays.svg')
  
    bone = os.fspath(solid_dir / 'bone.svg')
  
    clipboard_check = os.fspath(solid_dir / 'clipboard-check.svg')
  
    arrow_down_a_z = os.fspath(solid_dir / 'arrow-down-a-z.svg')
  
    circle_dollar_to_slot = os.fspath(solid_dir / 'circle-dollar-to-slot.svg')
  
    memory = os.fspath(solid_dir / 'memory.svg')
  
    circle_dot = os.fspath(solid_dir / 'circle-dot.svg')
  
    ice_cream = os.fspath(solid_dir / 'ice-cream.svg')
  
    hand_holding_droplet = os.fspath(solid_dir / 'hand-holding-droplet.svg')
  
    box = os.fspath(solid_dir / 'box.svg')
  
    file_video = os.fspath(solid_dir / 'file-video.svg')
  
    wine_glass_empty = os.fspath(solid_dir / 'wine-glass-empty.svg')
  
    hourglass_half = os.fspath(solid_dir / 'hourglass-half.svg')
  
    chevron_down = os.fspath(solid_dir / 'chevron-down.svg')
  
    camera_retro = os.fspath(solid_dir / 'camera-retro.svg')
  
    database = os.fspath(solid_dir / 'database.svg')
  
    arrow_up_a_z = os.fspath(solid_dir / 'arrow-up-a-z.svg')
  
    chess_rook = os.fspath(solid_dir / 'chess-rook.svg')
  
    file_zipper = os.fspath(solid_dir / 'file-zipper.svg')
  
    faucet = os.fspath(solid_dir / 'faucet.svg')
  
    users = os.fspath(solid_dir / 'users.svg')
  
    user_slash = os.fspath(solid_dir / 'user-slash.svg')
  
    tent_arrows_down = os.fspath(solid_dir / 'tent-arrows-down.svg')
  
    recycle = os.fspath(solid_dir / 'recycle.svg')
  
    scale_balanced = os.fspath(solid_dir / 'scale-balanced.svg')
  
    smog = os.fspath(solid_dir / 'smog.svg')
  
    paperclip = os.fspath(solid_dir / 'paperclip.svg')
  
    wind = os.fspath(solid_dir / 'wind.svg')
  
    tenge_sign = os.fspath(solid_dir / 'tenge-sign.svg')
  
    temperature_half = os.fspath(solid_dir / 'temperature-half.svg')
  
    tornado = os.fspath(solid_dir / 'tornado.svg')
  
    blog = os.fspath(solid_dir / 'blog.svg')
  
    arrows_up_to_line = os.fspath(solid_dir / 'arrows-up-to-line.svg')
  
    feather = os.fspath(solid_dir / 'feather.svg')
  
    comments = os.fspath(solid_dir / 'comments.svg')
  
    venus = os.fspath(solid_dir / 'venus.svg')
  
    tree_city = os.fspath(solid_dir / 'tree-city.svg')
  
    truck_front = os.fspath(solid_dir / 'truck-front.svg')
  
    handshake_slash = os.fspath(solid_dir / 'handshake-slash.svg')
  
    book_tanakh = os.fspath(solid_dir / 'book-tanakh.svg')
  
    rss = os.fspath(solid_dir / 'rss.svg')
  
    clapperboard = os.fspath(solid_dir / 'clapperboard.svg')
  
    sheet_plastic = os.fspath(solid_dir / 'sheet-plastic.svg')
  
    arrow_right = os.fspath(solid_dir / 'arrow-right.svg')
  
    sailboat = os.fspath(solid_dir / 'sailboat.svg')
  
    shower = os.fspath(solid_dir / 'shower.svg')
  
    left_long = os.fspath(solid_dir / 'left-long.svg')
  
    face_grimace = os.fspath(solid_dir / 'face-grimace.svg')
  
    circle_left = os.fspath(solid_dir / 'circle-left.svg')
  
    eye_slash = os.fspath(solid_dir / 'eye-slash.svg')
  
    bus_simple = os.fspath(solid_dir / 'bus-simple.svg')
  
    border_none = os.fspath(solid_dir / 'border-none.svg')
  
    person_dots_from_line = os.fspath(solid_dir / 'person-dots-from-line.svg')
  
    school_circle_check = os.fspath(solid_dir / 'school-circle-check.svg')
  
    right_long = os.fspath(solid_dir / 'right-long.svg')
  
    hurricane = os.fspath(solid_dir / 'hurricane.svg')
  
    trowel_bricks = os.fspath(solid_dir / 'trowel-bricks.svg')
  
    cubes_stacked = os.fspath(solid_dir / 'cubes-stacked.svg')
  
    temperature_arrow_down = os.fspath(solid_dir / 'temperature-arrow-down.svg')
  
    headphones = os.fspath(solid_dir / 'headphones.svg')
  
    cart_arrow_down = os.fspath(solid_dir / 'cart-arrow-down.svg')
  
    mill_sign = os.fspath(solid_dir / 'mill-sign.svg')
  
    bridge_circle_xmark = os.fspath(solid_dir / 'bridge-circle-xmark.svg')
  
    stairs = os.fspath(solid_dir / 'stairs.svg')
  
    gas_pump = os.fspath(solid_dir / 'gas-pump.svg')
  
    arrow_down_up_across_line = os.fspath(solid_dir / 'arrow-down-up-across-line.svg')
  
    rocket = os.fspath(solid_dir / 'rocket.svg')
  
    volume_high = os.fspath(solid_dir / 'volume-high.svg')
  
    text_slash = os.fspath(solid_dir / 'text-slash.svg')
  
    circle_play = os.fspath(solid_dir / 'circle-play.svg')
  
    hand_peace = os.fspath(solid_dir / 'hand-peace.svg')
  
    water_ladder = os.fspath(solid_dir / 'water-ladder.svg')
  
    user_xmark = os.fspath(solid_dir / 'user-xmark.svg')
  
    arrows_up_down = os.fspath(solid_dir / 'arrows-up-down.svg')
  
    globe = os.fspath(solid_dir / 'globe.svg')
  
    earth_africa = os.fspath(solid_dir / 'earth-africa.svg')
  
    truck_pickup = os.fspath(solid_dir / 'truck-pickup.svg')
  
    car_battery = os.fspath(solid_dir / 'car-battery.svg')
  
    poo = os.fspath(solid_dir / 'poo.svg')
  
    gavel = os.fspath(solid_dir / 'gavel.svg')
  
    beer_mug_empty = os.fspath(solid_dir / 'beer-mug-empty.svg')
  
    list = os.fspath(solid_dir / 'list.svg')
  
    plane_arrival = os.fspath(solid_dir / 'plane-arrival.svg')
  
    file_invoice = os.fspath(solid_dir / 'file-invoice.svg')
  
    child_combatant = os.fspath(solid_dir / 'child-combatant.svg')
  
    award = os.fspath(solid_dir / 'award.svg')
  
    lari_sign = os.fspath(solid_dir / 'lari-sign.svg')
  
    person_rays = os.fspath(solid_dir / 'person-rays.svg')
  
    circle_up = os.fspath(solid_dir / 'circle-up.svg')
  
    podcast = os.fspath(solid_dir / 'podcast.svg')
  
    temperature_low = os.fspath(solid_dir / 'temperature-low.svg')
  
    landmark_flag = os.fspath(solid_dir / 'landmark-flag.svg')
  
    medal = os.fspath(solid_dir / 'medal.svg')
  
    capsules = os.fspath(solid_dir / 'capsules.svg')
  
    plane_slash = os.fspath(solid_dir / 'plane-slash.svg')
  
    hand_pointer = os.fspath(solid_dir / 'hand-pointer.svg')
  
    arrow_down_z_a = os.fspath(solid_dir / 'arrow-down-z-a.svg')
  
    dong_sign = os.fspath(solid_dir / 'dong-sign.svg')
  
    droplet_slash = os.fspath(solid_dir / 'droplet-slash.svg')
  
    person_arrow_up_from_line = os.fspath(solid_dir / 'person-arrow-up-from-line.svg')
  
    handcuffs = os.fspath(solid_dir / 'handcuffs.svg')
  
    _0 = os.fspath(solid_dir / '0.svg')
  
    shekel_sign = os.fspath(solid_dir / 'shekel-sign.svg')
  
    cross = os.fspath(solid_dir / 'cross.svg')
  
    stethoscope = os.fspath(solid_dir / 'stethoscope.svg')
  
    filter = os.fspath(solid_dir / 'filter.svg')
  
    copyright = os.fspath(solid_dir / 'copyright.svg')
  
    people_line = os.fspath(solid_dir / 'people-line.svg')
  
    pen_fancy = os.fspath(solid_dir / 'pen-fancy.svg')
  
    headphones_simple = os.fspath(solid_dir / 'headphones-simple.svg')
  
    calendar_plus = os.fspath(solid_dir / 'calendar-plus.svg')
  
    infinity = os.fspath(solid_dir / 'infinity.svg')
  
    ruler_horizontal = os.fspath(solid_dir / 'ruler-horizontal.svg')
  
    pen = os.fspath(solid_dir / 'pen.svg')
  
    map_pin = os.fspath(solid_dir / 'map-pin.svg')
  
    person_half_dress = os.fspath(solid_dir / 'person-half-dress.svg')
  
    share_nodes = os.fspath(solid_dir / 'share-nodes.svg')
  
    virus_covid = os.fspath(solid_dir / 'virus-covid.svg')
  
    house_circle_xmark = os.fspath(solid_dir / 'house-circle-xmark.svg')
  
    arrow_rotate_left = os.fspath(solid_dir / 'arrow-rotate-left.svg')
  
    book_bible = os.fspath(solid_dir / 'book-bible.svg')
  
    life_ring = os.fspath(solid_dir / 'life-ring.svg')
  
    trademark = os.fspath(solid_dir / 'trademark.svg')
  
    file_pdf = os.fspath(solid_dir / 'file-pdf.svg')
  
    person_skating = os.fspath(solid_dir / 'person-skating.svg')
  
    poo_storm = os.fspath(solid_dir / 'poo-storm.svg')
  
    paragraph = os.fspath(solid_dir / 'paragraph.svg')
  
    location_crosshairs = os.fspath(solid_dir / 'location-crosshairs.svg')
  
    pills = os.fspath(solid_dir / 'pills.svg')
  
    mars_stroke_up = os.fspath(solid_dir / 'mars-stroke-up.svg')
  
    horse_head = os.fspath(solid_dir / 'horse-head.svg')
  
    user_graduate = os.fspath(solid_dir / 'user-graduate.svg')
  
    hand_scissors = os.fspath(solid_dir / 'hand-scissors.svg')
  
    suitcase_medical = os.fspath(solid_dir / 'suitcase-medical.svg')
  
    e = os.fspath(solid_dir / 'e.svg')
  
    bicycle = os.fspath(solid_dir / 'bicycle.svg')
  
    caret_left = os.fspath(solid_dir / 'caret-left.svg')
  
    hard_drive = os.fspath(solid_dir / 'hard-drive.svg')
  
    house_chimney = os.fspath(solid_dir / 'house-chimney.svg')
  
    wheelchair = os.fspath(solid_dir / 'wheelchair.svg')
  
    meteor = os.fspath(solid_dir / 'meteor.svg')
  
    road = os.fspath(solid_dir / 'road.svg')
  
    suitcase = os.fspath(solid_dir / 'suitcase.svg')
  
    cloud_arrow_down = os.fspath(solid_dir / 'cloud-arrow-down.svg')
  
    helmet_un = os.fspath(solid_dir / 'helmet-un.svg')
  
    truck_droplet = os.fspath(solid_dir / 'truck-droplet.svg')
  
    circle_user = os.fspath(solid_dir / 'circle-user.svg')
  
    equals = os.fspath(solid_dir / 'equals.svg')
  
    genderless = os.fspath(solid_dir / 'genderless.svg')
  
    money_bill_wave = os.fspath(solid_dir / 'money-bill-wave.svg')
  
    vector_square = os.fspath(solid_dir / 'vector-square.svg')
  
    compass_drafting = os.fspath(solid_dir / 'compass-drafting.svg')
  
    z = os.fspath(solid_dir / 'z.svg')
  
    cloud_showers_water = os.fspath(solid_dir / 'cloud-showers-water.svg')
  
    chess_king = os.fspath(solid_dir / 'chess-king.svg')
  
    fire_extinguisher = os.fspath(solid_dir / 'fire-extinguisher.svg')
  
    vial = os.fspath(solid_dir / 'vial.svg')
  
    champagne_glasses = os.fspath(solid_dir / 'champagne-glasses.svg')
  
    person_praying = os.fspath(solid_dir / 'person-praying.svg')
  
    camera = os.fspath(solid_dir / 'camera.svg')
  
    bacterium = os.fspath(solid_dir / 'bacterium.svg')
  
    sliders = os.fspath(solid_dir / 'sliders.svg')
  
    pump_medical = os.fspath(solid_dir / 'pump-medical.svg')
  
    money_check = os.fspath(solid_dir / 'money-check.svg')
  
    jar_wheat = os.fspath(solid_dir / 'jar-wheat.svg')
  
    file_shield = os.fspath(solid_dir / 'file-shield.svg')
  
    heart_circle_minus = os.fspath(solid_dir / 'heart-circle-minus.svg')
  
    person_walking = os.fspath(solid_dir / 'person-walking.svg')
  
    file_circle_exclamation = os.fspath(solid_dir / 'file-circle-exclamation.svg')
  
    hands = os.fspath(solid_dir / 'hands.svg')
  
    r = os.fspath(solid_dir / 'r.svg')
  
    dice = os.fspath(solid_dir / 'dice.svg')
  
    eject = os.fspath(solid_dir / 'eject.svg')
  
    face_kiss_wink_heart = os.fspath(solid_dir / 'face-kiss-wink-heart.svg')
  
    baseball_bat_ball = os.fspath(solid_dir / 'baseball-bat-ball.svg')
  
    gauge_high = os.fspath(solid_dir / 'gauge-high.svg')
  
    server = os.fspath(solid_dir / 'server.svg')
  
    rupiah_sign = os.fspath(solid_dir / 'rupiah-sign.svg')
  
    hand_point_left = os.fspath(solid_dir / 'hand-point-left.svg')
  
    backward_fast = os.fspath(solid_dir / 'backward-fast.svg')
  
    ribbon = os.fspath(solid_dir / 'ribbon.svg')
  
    cable_car = os.fspath(solid_dir / 'cable-car.svg')
  
    video_slash = os.fspath(solid_dir / 'video-slash.svg')
  
    tent_arrow_turn_left = os.fspath(solid_dir / 'tent-arrow-turn-left.svg')
  
    hryvnia_sign = os.fspath(solid_dir / 'hryvnia-sign.svg')
  
    splotch = os.fspath(solid_dir / 'splotch.svg')
  
    bus = os.fspath(solid_dir / 'bus.svg')
  
    motorcycle = os.fspath(solid_dir / 'motorcycle.svg')
  
    oil_can = os.fspath(solid_dir / 'oil-can.svg')
  
    ticket_simple = os.fspath(solid_dir / 'ticket-simple.svg')
  
    grip_lines_vertical = os.fspath(solid_dir / 'grip-lines-vertical.svg')
  
    arrow_right_to_bracket = os.fspath(solid_dir / 'arrow-right-to-bracket.svg')
  
    bore_hole = os.fspath(solid_dir / 'bore-hole.svg')
  
    arrow_up_z_a = os.fspath(solid_dir / 'arrow-up-z-a.svg')
  
    person_walking_dashed_line_arrow_right = os.fspath(solid_dir / 'person-walking-dashed-line-arrow-right.svg')
  
    headset = os.fspath(solid_dir / 'headset.svg')
  
    left_right = os.fspath(solid_dir / 'left-right.svg')
  
    magnet = os.fspath(solid_dir / 'magnet.svg')
  
    flag_usa = os.fspath(solid_dir / 'flag-usa.svg')
  
    person_harassing = os.fspath(solid_dir / 'person-harassing.svg')
  
    hat_cowboy = os.fspath(solid_dir / 'hat-cowboy.svg')
  
    flask_vial = os.fspath(solid_dir / 'flask-vial.svg')
  
    circle_down = os.fspath(solid_dir / 'circle-down.svg')
  
    clock = os.fspath(solid_dir / 'clock.svg')
  
    camera_rotate = os.fspath(solid_dir / 'camera-rotate.svg')
  
    hospital_user = os.fspath(solid_dir / 'hospital-user.svg')
  
    crop_simple = os.fspath(solid_dir / 'crop-simple.svg')
  
    explosion = os.fspath(solid_dir / 'explosion.svg')
  
    section = os.fspath(solid_dir / 'section.svg')
  
    folder_tree = os.fspath(solid_dir / 'folder-tree.svg')
  
    book_quran = os.fspath(solid_dir / 'book-quran.svg')
  
    expand = os.fspath(solid_dir / 'expand.svg')
  
    arrow_right_arrow_left = os.fspath(solid_dir / 'arrow-right-arrow-left.svg')
  
    austral_sign = os.fspath(solid_dir / 'austral-sign.svg')
  
    a = os.fspath(solid_dir / 'a.svg')
  
    mobile = os.fspath(solid_dir / 'mobile.svg')
  
    puzzle_piece = os.fspath(solid_dir / 'puzzle-piece.svg')
  
    list_ul = os.fspath(solid_dir / 'list-ul.svg')
  
    _8 = os.fspath(solid_dir / '8.svg')
  
    divide = os.fspath(solid_dir / 'divide.svg')
  
    jedi = os.fspath(solid_dir / 'jedi.svg')
  
    mug_saucer = os.fspath(solid_dir / 'mug-saucer.svg')
  
    arrow_up_1_9 = os.fspath(solid_dir / 'arrow-up-1-9.svg')
  
    person_falling = os.fspath(solid_dir / 'person-falling.svg')
  
    thumbtack = os.fspath(solid_dir / 'thumbtack.svg')
  
    person_circle_minus = os.fspath(solid_dir / 'person-circle-minus.svg')
  
    angle_right = os.fspath(solid_dir / 'angle-right.svg')
  
    folder = os.fspath(solid_dir / 'folder.svg')
  
    window_restore = os.fspath(solid_dir / 'window-restore.svg')
  
    child_reaching = os.fspath(solid_dir / 'child-reaching.svg')
  
    mask_ventilator = os.fspath(solid_dir / 'mask-ventilator.svg')
  
    bookmark = os.fspath(solid_dir / 'bookmark.svg')
  
    voicemail = os.fspath(solid_dir / 'voicemail.svg')
  
    fish_fins = os.fspath(solid_dir / 'fish-fins.svg')
  
    icicles = os.fspath(solid_dir / 'icicles.svg')
  
    shoe_prints = os.fspath(solid_dir / 'shoe-prints.svg')
  
    house_user = os.fspath(solid_dir / 'house-user.svg')
  
    location_pin = os.fspath(solid_dir / 'location-pin.svg')
  
    at = os.fspath(solid_dir / 'at.svg')
  
    shield_dog = os.fspath(solid_dir / 'shield-dog.svg')
  
    trash_can_arrow_up = os.fspath(solid_dir / 'trash-can-arrow-up.svg')
  
    dice_three = os.fspath(solid_dir / 'dice-three.svg')
  
    magnifying_glass_dollar = os.fspath(solid_dir / 'magnifying-glass-dollar.svg')
  
    vr_cardboard = os.fspath(solid_dir / 'vr-cardboard.svg')
  
    location_arrow = os.fspath(solid_dir / 'location-arrow.svg')
  
    hockey_puck = os.fspath(solid_dir / 'hockey-puck.svg')
  
    diagram_project = os.fspath(solid_dir / 'diagram-project.svg')
  
    bread_slice = os.fspath(solid_dir / 'bread-slice.svg')
  
    user_clock = os.fspath(solid_dir / 'user-clock.svg')
  
    street_view = os.fspath(solid_dir / 'street-view.svg')
  
    bug = os.fspath(solid_dir / 'bug.svg')
  
    book_medical = os.fspath(solid_dir / 'book-medical.svg')
  
    t = os.fspath(solid_dir / 't.svg')
  
    up_right_and_down_left_from_center = os.fspath(solid_dir / 'up-right-and-down-left-from-center.svg')
  
    up_down = os.fspath(solid_dir / 'up-down.svg')
  
    compact_disc = os.fspath(solid_dir / 'compact-disc.svg')
  
    chess_pawn = os.fspath(solid_dir / 'chess-pawn.svg')
  
    image_portrait = os.fspath(solid_dir / 'image-portrait.svg')
  
    swatchbook = os.fspath(solid_dir / 'swatchbook.svg')
  
    brazilian_real_sign = os.fspath(solid_dir / 'brazilian-real-sign.svg')
  
    building_circle_exclamation = os.fspath(solid_dir / 'building-circle-exclamation.svg')
  
    forward_fast = os.fspath(solid_dir / 'forward-fast.svg')
  
    archway = os.fspath(solid_dir / 'archway.svg')
  
    users_viewfinder = os.fspath(solid_dir / 'users-viewfinder.svg')
  
    circle_check = os.fspath(solid_dir / 'circle-check.svg')
  
    clone = os.fspath(solid_dir / 'clone.svg')
  
    arrow_down_up_lock = os.fspath(solid_dir / 'arrow-down-up-lock.svg')
  
    person_walking_arrow_right = os.fspath(solid_dir / 'person-walking-arrow-right.svg')
  
    house_flood_water_circle_arrow_right = os.fspath(solid_dir / 'house-flood-water-circle-arrow-right.svg')
  
    square_poll_horizontal = os.fspath(solid_dir / 'square-poll-horizontal.svg')
  
    less_than = os.fspath(solid_dir / 'less-than.svg')
  
    hourglass_start = os.fspath(solid_dir / 'hourglass-start.svg')
  
    language = os.fspath(solid_dir / 'language.svg')
  
    envelope_open = os.fspath(solid_dir / 'envelope-open.svg')
  
    house_fire = os.fspath(solid_dir / 'house-fire.svg')
  
    user_tag = os.fspath(solid_dir / 'user-tag.svg')
  
    glass_water_droplet = os.fspath(solid_dir / 'glass-water-droplet.svg')
  
    plane_lock = os.fspath(solid_dir / 'plane-lock.svg')
  
    lungs = os.fspath(solid_dir / 'lungs.svg')
  
    elevator = os.fspath(solid_dir / 'elevator.svg')
  
    hashtag = os.fspath(solid_dir / 'hashtag.svg')
  
    temperature_three_quarters = os.fspath(solid_dir / 'temperature-three-quarters.svg')
  
    building_circle_xmark = os.fspath(solid_dir / 'building-circle-xmark.svg')
  
    plus = os.fspath(solid_dir / 'plus.svg')
  
    biohazard = os.fspath(solid_dir / 'biohazard.svg')
  
    shirt = os.fspath(solid_dir / 'shirt.svg')
  
    colon_sign = os.fspath(solid_dir / 'colon-sign.svg')
  
    baseball = os.fspath(solid_dir / 'baseball.svg')
  
    flag_checkered = os.fspath(solid_dir / 'flag-checkered.svg')
  
    address_book = os.fspath(solid_dir / 'address-book.svg')
  
    venus_double = os.fspath(solid_dir / 'venus-double.svg')
  
    asterisk = os.fspath(solid_dir / 'asterisk.svg')
  
    file_export = os.fspath(solid_dir / 'file-export.svg')
  
    palette = os.fspath(solid_dir / 'palette.svg')
  
    link_slash = os.fspath(solid_dir / 'link-slash.svg')
  
    money_bill = os.fspath(solid_dir / 'money-bill.svg')
  
    rotate_left = os.fspath(solid_dir / 'rotate-left.svg')
  
    circle_info = os.fspath(solid_dir / 'circle-info.svg')
  
    vault = os.fspath(solid_dir / 'vault.svg')
  
    turkish_lira_sign = os.fspath(solid_dir / 'turkish-lira-sign.svg')
  
    square_phone = os.fspath(solid_dir / 'square-phone.svg')
  
    toilet = os.fspath(solid_dir / 'toilet.svg')
  
    person_rifle = os.fspath(solid_dir / 'person-rifle.svg')
  
    bitcoin_sign = os.fspath(solid_dir / 'bitcoin-sign.svg')
  
    person_circle_check = os.fspath(solid_dir / 'person-circle-check.svg')
  
    stamp = os.fspath(solid_dir / 'stamp.svg')
  
    bottle_droplet = os.fspath(solid_dir / 'bottle-droplet.svg')
  
    golf_ball_tee = os.fspath(solid_dir / 'golf-ball-tee.svg')
  
    code_compare = os.fspath(solid_dir / 'code-compare.svg')
  
    school_flag = os.fspath(solid_dir / 'school-flag.svg')
  
    face_grin_hearts = os.fspath(solid_dir / 'face-grin-hearts.svg')
  
    sort = os.fspath(solid_dir / 'sort.svg')
  
    square_plus = os.fspath(solid_dir / 'square-plus.svg')
  
    gopuram = os.fspath(solid_dir / 'gopuram.svg')
  
    head_side_cough_slash = os.fspath(solid_dir / 'head-side-cough-slash.svg')
  
    gift = os.fspath(solid_dir / 'gift.svg')
  
    chevron_left = os.fspath(solid_dir / 'chevron-left.svg')
  
    hospital = os.fspath(solid_dir / 'hospital.svg')
  
    wand_magic_sparkles = os.fspath(solid_dir / 'wand-magic-sparkles.svg')
  
    arrows_left_right = os.fspath(solid_dir / 'arrows-left-right.svg')
  
    users_slash = os.fspath(solid_dir / 'users-slash.svg')
  
    om = os.fspath(solid_dir / 'om.svg')
  
    universal_access = os.fspath(solid_dir / 'universal-access.svg')
  
    record_vinyl = os.fspath(solid_dir / 'record-vinyl.svg')
  
    box_tissue = os.fspath(solid_dir / 'box-tissue.svg')
  
    underline = os.fspath(solid_dir / 'underline.svg')
  
    file_csv = os.fspath(solid_dir / 'file-csv.svg')
  
    water = os.fspath(solid_dir / 'water.svg')
  
    heart_circle_check = os.fspath(solid_dir / 'heart-circle-check.svg')
  
    circle_arrow_down = os.fspath(solid_dir / 'circle-arrow-down.svg')
  
    hat_wizard = os.fspath(solid_dir / 'hat-wizard.svg')
  
    floppy_disk = os.fspath(solid_dir / 'floppy-disk.svg')
  
    file_word = os.fspath(solid_dir / 'file-word.svg')
  
    location_pin_lock = os.fspath(solid_dir / 'location-pin-lock.svg')
  
    magnifying_glass_minus = os.fspath(solid_dir / 'magnifying-glass-minus.svg')
  
    road_bridge = os.fspath(solid_dir / 'road-bridge.svg')
  
    chevron_right = os.fspath(solid_dir / 'chevron-right.svg')
  
    cart_shopping = os.fspath(solid_dir / 'cart-shopping.svg')
  
    star_half = os.fspath(solid_dir / 'star-half.svg')
  
    clipboard_list = os.fspath(solid_dir / 'clipboard-list.svg')
  
    person_military_to_person = os.fspath(solid_dir / 'person-military-to-person.svg')
  
    retweet = os.fspath(solid_dir / 'retweet.svg')
  
    person_circle_exclamation = os.fspath(solid_dir / 'person-circle-exclamation.svg')
  
    newspaper = os.fspath(solid_dir / 'newspaper.svg')
  
    calendar_check = os.fspath(solid_dir / 'calendar-check.svg')
  
    comment_dots = os.fspath(solid_dir / 'comment-dots.svg')
  
    star_and_crescent = os.fspath(solid_dir / 'star-and-crescent.svg')
  
    user_nurse = os.fspath(solid_dir / 'user-nurse.svg')
  
    sun = os.fspath(solid_dir / 'sun.svg')
  
    down_left_and_up_right_to_center = os.fspath(solid_dir / 'down-left-and-up-right-to-center.svg')
  
    cannabis = os.fspath(solid_dir / 'cannabis.svg')
  
    tachograph_digital = os.fspath(solid_dir / 'tachograph-digital.svg')
  
    phone_slash = os.fspath(solid_dir / 'phone-slash.svg')
  
    circle_right = os.fspath(solid_dir / 'circle-right.svg')
  
    store = os.fspath(solid_dir / 'store.svg')
  
    envelope = os.fspath(solid_dir / 'envelope.svg')
  
    microphone_slash = os.fspath(solid_dir / 'microphone-slash.svg')
  
    eye_low_vision = os.fspath(solid_dir / 'eye-low-vision.svg')
  
    chart_column = os.fspath(solid_dir / 'chart-column.svg')
  
    paste = os.fspath(solid_dir / 'paste.svg')
  
    drum = os.fspath(solid_dir / 'drum.svg')
  
    house_tsunami = os.fspath(solid_dir / 'house-tsunami.svg')
  
    disease = os.fspath(solid_dir / 'disease.svg')
  
    mask = os.fspath(solid_dir / 'mask.svg')
  
    info = os.fspath(solid_dir / 'info.svg')
  
    sd_card = os.fspath(solid_dir / 'sd-card.svg')
  
    square_nfi = os.fspath(solid_dir / 'square-nfi.svg')
  
    link = os.fspath(solid_dir / 'link.svg')
  
    upload = os.fspath(solid_dir / 'upload.svg')
  
    face_smile_wink = os.fspath(solid_dir / 'face-smile-wink.svg')
  
    volcano = os.fspath(solid_dir / 'volcano.svg')
  
    up_right_from_square = os.fspath(solid_dir / 'up-right-from-square.svg')
  
    pepper_hot = os.fspath(solid_dir / 'pepper-hot.svg')
  
    mars = os.fspath(solid_dir / 'mars.svg')
  
    wand_magic = os.fspath(solid_dir / 'wand-magic.svg')
  
    crutch = os.fspath(solid_dir / 'crutch.svg')
  
    music = os.fspath(solid_dir / 'music.svg')
  
    lira_sign = os.fspath(solid_dir / 'lira-sign.svg')
  
    menorah = os.fspath(solid_dir / 'menorah.svg')
  
    angles_down = os.fspath(solid_dir / 'angles-down.svg')
  
    house_flood_water = os.fspath(solid_dir / 'house-flood-water.svg')
  
    dog = os.fspath(solid_dir / 'dog.svg')
  
    n = os.fspath(solid_dir / 'n.svg')
  
    anchor_circle_check = os.fspath(solid_dir / 'anchor-circle-check.svg')
  
    bong = os.fspath(solid_dir / 'bong.svg')
  
    text_width = os.fspath(solid_dir / 'text-width.svg')
  
    arrows_turn_right = os.fspath(solid_dir / 'arrows-turn-right.svg')
  
    arrow_up = os.fspath(solid_dir / 'arrow-up.svg')
  
    circle_plus = os.fspath(solid_dir / 'circle-plus.svg')
  
    chart_gantt = os.fspath(solid_dir / 'chart-gantt.svg')
  
    greater_than = os.fspath(solid_dir / 'greater-than.svg')
  
    forward_step = os.fspath(solid_dir / 'forward-step.svg')
  
    u = os.fspath(solid_dir / 'u.svg')
  
    briefcase = os.fspath(solid_dir / 'briefcase.svg')
  
    microscope = os.fspath(solid_dir / 'microscope.svg')
  
    caravan = os.fspath(solid_dir / 'caravan.svg')
  
    plate_wheat = os.fspath(solid_dir / 'plate-wheat.svg')
  
    clipboard = os.fspath(solid_dir / 'clipboard.svg')
  
    user_doctor = os.fspath(solid_dir / 'user-doctor.svg')
  
    square_minus = os.fspath(solid_dir / 'square-minus.svg')
  
    hand_sparkles = os.fspath(solid_dir / 'hand-sparkles.svg')
  
    truck_moving = os.fspath(solid_dir / 'truck-moving.svg')
  
    school_lock = os.fspath(solid_dir / 'school-lock.svg')
  
    prescription_bottle = os.fspath(solid_dir / 'prescription-bottle.svg')
  
    sleigh = os.fspath(solid_dir / 'sleigh.svg')
  
    tag = os.fspath(solid_dir / 'tag.svg')
  
    stapler = os.fspath(solid_dir / 'stapler.svg')
  
    check_double = os.fspath(solid_dir / 'check-double.svg')
  
    audio_description = os.fspath(solid_dir / 'audio-description.svg')
  
    charging_station = os.fspath(solid_dir / 'charging-station.svg')
  
    bridge = os.fspath(solid_dir / 'bridge.svg')
  
    plug_circle_bolt = os.fspath(solid_dir / 'plug-circle-bolt.svg')
  
    hamsa = os.fspath(solid_dir / 'hamsa.svg')
  
    bahai = os.fspath(solid_dir / 'bahai.svg')
  
    circle_arrow_up = os.fspath(solid_dir / 'circle-arrow-up.svg')
  
    m = os.fspath(solid_dir / 'm.svg')
  
    star = os.fspath(solid_dir / 'star.svg')
  
    head_side_cough = os.fspath(solid_dir / 'head-side-cough.svg')
  
    arrow_up_from_water_pump = os.fspath(solid_dir / 'arrow-up-from-water-pump.svg')
  
    road_spikes = os.fspath(solid_dir / 'road-spikes.svg')
  
    battery_quarter = os.fspath(solid_dir / 'battery-quarter.svg')
  
    solar_panel = os.fspath(solid_dir / 'solar-panel.svg')
  
    laptop_medical = os.fspath(solid_dir / 'laptop-medical.svg')
  
    align_center = os.fspath(solid_dir / 'align-center.svg')
  
    circle_pause = os.fspath(solid_dir / 'circle-pause.svg')
  
    forward = os.fspath(solid_dir / 'forward.svg')
  
    circle_arrow_left = os.fspath(solid_dir / 'circle-arrow-left.svg')
  
    panorama = os.fspath(solid_dir / 'panorama.svg')
  
    hotel = os.fspath(solid_dir / 'hotel.svg')
  
    grip_vertical = os.fspath(solid_dir / 'grip-vertical.svg')
  
    tower_observation = os.fspath(solid_dir / 'tower-observation.svg')
  
    virus = os.fspath(solid_dir / 'virus.svg')
  
    fan = os.fspath(solid_dir / 'fan.svg')
  
    shield_virus = os.fspath(solid_dir / 'shield-virus.svg')
  
    square = os.fspath(solid_dir / 'square.svg')
  
    soap = os.fspath(solid_dir / 'soap.svg')
  
    martini_glass_empty = os.fspath(solid_dir / 'martini-glass-empty.svg')
  
    indent = os.fspath(solid_dir / 'indent.svg')
  
    flag = os.fspath(solid_dir / 'flag.svg')
  
    tablet_screen_button = os.fspath(solid_dir / 'tablet-screen-button.svg')
  
    satellite_dish = os.fspath(solid_dir / 'satellite-dish.svg')
  
    video = os.fspath(solid_dir / 'video.svg')
  
    users_between_lines = os.fspath(solid_dir / 'users-between-lines.svg')
  
    mars_double = os.fspath(solid_dir / 'mars-double.svg')
  
    sterling_sign = os.fspath(solid_dir / 'sterling-sign.svg')
  
    bars_staggered = os.fspath(solid_dir / 'bars-staggered.svg')
  
    manat_sign = os.fspath(solid_dir / 'manat-sign.svg')
  
    barcode = os.fspath(solid_dir / 'barcode.svg')
  
    face_kiss_beam = os.fspath(solid_dir / 'face-kiss-beam.svg')
  
    wheat_awn_circle_exclamation = os.fspath(solid_dir / 'wheat-awn-circle-exclamation.svg')
  
    anchor_circle_xmark = os.fspath(solid_dir / 'anchor-circle-xmark.svg')
  
    handshake_simple = os.fspath(solid_dir / 'handshake-simple.svg')
  
    florin_sign = os.fspath(solid_dir / 'florin-sign.svg')
  
    address_card = os.fspath(solid_dir / 'address-card.svg')
  
    square_xmark = os.fspath(solid_dir / 'square-xmark.svg')
  
    arrows_to_dot = os.fspath(solid_dir / 'arrows-to-dot.svg')
  
    prescription_bottle_medical = os.fspath(solid_dir / 'prescription-bottle-medical.svg')
  
    cat = os.fspath(solid_dir / 'cat.svg')
  
    snowplow = os.fspath(solid_dir / 'snowplow.svg')
  
    vial_virus = os.fspath(solid_dir / 'vial-virus.svg')
  
    couch = os.fspath(solid_dir / 'couch.svg')
  
    square_phone_flip = os.fspath(solid_dir / 'square-phone-flip.svg')
  
    cheese = os.fspath(solid_dir / 'cheese.svg')
  
    id_badge = os.fspath(solid_dir / 'id-badge.svg')
  
    file_contract = os.fspath(solid_dir / 'file-contract.svg')
  
    star_of_life = os.fspath(solid_dir / 'star-of-life.svg')
  
    bowling_ball = os.fspath(solid_dir / 'bowling-ball.svg')
  
    crosshairs = os.fspath(solid_dir / 'crosshairs.svg')
  
    shop_slash = os.fspath(solid_dir / 'shop-slash.svg')
  
    file_circle_plus = os.fspath(solid_dir / 'file-circle-plus.svg')
  
    anchor_circle_exclamation = os.fspath(solid_dir / 'anchor-circle-exclamation.svg')
  
    arrow_up_from_ground_water = os.fspath(solid_dir / 'arrow-up-from-ground-water.svg')
  
    road_circle_check = os.fspath(solid_dir / 'road-circle-check.svg')
  
    shield_heart = os.fspath(solid_dir / 'shield-heart.svg')
  
    q = os.fspath(solid_dir / 'q.svg')
  
    house_medical = os.fspath(solid_dir / 'house-medical.svg')
  
    guarani_sign = os.fspath(solid_dir / 'guarani-sign.svg')
  
    user = os.fspath(solid_dir / 'user.svg')
  
    gauge_simple_high = os.fspath(solid_dir / 'gauge-simple-high.svg')
  
    tablets = os.fspath(solid_dir / 'tablets.svg')
  
    certificate = os.fspath(solid_dir / 'certificate.svg')
  
    person_military_rifle = os.fspath(solid_dir / 'person-military-rifle.svg')
  
    scale_unbalanced_flip = os.fspath(solid_dir / 'scale-unbalanced-flip.svg')
  
    hourglass = os.fspath(solid_dir / 'hourglass.svg')
  
    heart_pulse = os.fspath(solid_dir / 'heart-pulse.svg')
  
    sack_xmark = os.fspath(solid_dir / 'sack-xmark.svg')
  
    photo_film = os.fspath(solid_dir / 'photo-film.svg')
  
    arrow_turn_up = os.fspath(solid_dir / 'arrow-turn-up.svg')
  
    display = os.fspath(solid_dir / 'display.svg')
  
    mountain = os.fspath(solid_dir / 'mountain.svg')
  
    mortar_pestle = os.fspath(solid_dir / 'mortar-pestle.svg')
  
    building_wheat = os.fspath(solid_dir / 'building-wheat.svg')
  
    locust = os.fspath(solid_dir / 'locust.svg')
  
    vial_circle_check = os.fspath(solid_dir / 'vial-circle-check.svg')
  
    fill = os.fspath(solid_dir / 'fill.svg')
  
    angle_left = os.fspath(solid_dir / 'angle-left.svg')
  
    scroll_torah = os.fspath(solid_dir / 'scroll-torah.svg')
  
    flask = os.fspath(solid_dir / 'flask.svg')
  
    chair = os.fspath(solid_dir / 'chair.svg')
  
    calculator = os.fspath(solid_dir / 'calculator.svg')
  
    stroopwafel = os.fspath(solid_dir / 'stroopwafel.svg')
  
    film = os.fspath(solid_dir / 'film.svg')
  
    magnifying_glass_location = os.fspath(solid_dir / 'magnifying-glass-location.svg')
  
    battery_three_quarters = os.fspath(solid_dir / 'battery-three-quarters.svg')
  
    dolly = os.fspath(solid_dir / 'dolly.svg')
  
    _3 = os.fspath(solid_dir / '3.svg')
  
    vials = os.fspath(solid_dir / 'vials.svg')
  
    dice_d6 = os.fspath(solid_dir / 'dice-d6.svg')
  
    envelope_open_text = os.fspath(solid_dir / 'envelope-open-text.svg')
  
    user_plus = os.fspath(solid_dir / 'user-plus.svg')
  
    droplet = os.fspath(solid_dir / 'droplet.svg')
  
    volume_off = os.fspath(solid_dir / 'volume-off.svg')
  
    shield = os.fspath(solid_dir / 'shield.svg')
  
    _7 = os.fspath(solid_dir / '7.svg')
  
    city = os.fspath(solid_dir / 'city.svg')
  
    map_location_dot = os.fspath(solid_dir / 'map-location-dot.svg')
  
    user_gear = os.fspath(solid_dir / 'user-gear.svg')
  
    people_robbery = os.fspath(solid_dir / 'people-robbery.svg')
  
    horse = os.fspath(solid_dir / 'horse.svg')
  
    triangle_exclamation = os.fspath(solid_dir / 'triangle-exclamation.svg')
  
    v = os.fspath(solid_dir / 'v.svg')
  
    earth_asia = os.fspath(solid_dir / 'earth-asia.svg')
  
    hand_holding_heart = os.fspath(solid_dir / 'hand-holding-heart.svg')
  
    dna = os.fspath(solid_dir / 'dna.svg')
  
    hand_middle_finger = os.fspath(solid_dir / 'hand-middle-finger.svg')
  
    w = os.fspath(solid_dir / 'w.svg')
  
    pen_clip = os.fspath(solid_dir / 'pen-clip.svg')
  
    person_shelter = os.fspath(solid_dir / 'person-shelter.svg')
  
    mattress_pillow = os.fspath(solid_dir / 'mattress-pillow.svg')
  
    id_card_clip = os.fspath(solid_dir / 'id-card-clip.svg')
  
    franc_sign = os.fspath(solid_dir / 'franc-sign.svg')
  
    heart_circle_plus = os.fspath(solid_dir / 'heart-circle-plus.svg')
  
    list_check = os.fspath(solid_dir / 'list-check.svg')
  
    mountain_sun = os.fspath(solid_dir / 'mountain-sun.svg')
  
    glasses = os.fspath(solid_dir / 'glasses.svg')
  
    leaf = os.fspath(solid_dir / 'leaf.svg')
  
    chart_line = os.fspath(solid_dir / 'chart-line.svg')
  
    vest_patches = os.fspath(solid_dir / 'vest-patches.svg')
  
    wrench = os.fspath(solid_dir / 'wrench.svg')
  
    hand_holding_hand = os.fspath(solid_dir / 'hand-holding-hand.svg')
  
    bacteria = os.fspath(solid_dir / 'bacteria.svg')
  
    battery_full = os.fspath(solid_dir / 'battery-full.svg')
  
    square_parking = os.fspath(solid_dir / 'square-parking.svg')
  
    wine_bottle = os.fspath(solid_dir / 'wine-bottle.svg')
  
    cedi_sign = os.fspath(solid_dir / 'cedi-sign.svg')
  
    kaaba = os.fspath(solid_dir / 'kaaba.svg')
  
    circle_chevron_right = os.fspath(solid_dir / 'circle-chevron-right.svg')
  
    hands_praying = os.fspath(solid_dir / 'hands-praying.svg')
  
    book_skull = os.fspath(solid_dir / 'book-skull.svg')
  
    bowl_rice = os.fspath(solid_dir / 'bowl-rice.svg')
  
    italic = os.fspath(solid_dir / 'italic.svg')
  
    truck_field = os.fspath(solid_dir / 'truck-field.svg')
  
    calendar_day = os.fspath(solid_dir / 'calendar-day.svg')
  
    scissors = os.fspath(solid_dir / 'scissors.svg')
  
    handshake = os.fspath(solid_dir / 'handshake.svg')
  
    angles_up = os.fspath(solid_dir / 'angles-up.svg')
  
    ruler_vertical = os.fspath(solid_dir / 'ruler-vertical.svg')
  
    person_running = os.fspath(solid_dir / 'person-running.svg')
  
    building_flag = os.fspath(solid_dir / 'building-flag.svg')
  
    cookie_bite = os.fspath(solid_dir / 'cookie-bite.svg')
  
    house_chimney_user = os.fspath(solid_dir / 'house-chimney-user.svg')
  
    calendar_days = os.fspath(solid_dir / 'calendar-days.svg')
  
    user_pen = os.fspath(solid_dir / 'user-pen.svg')
  
    hands_bubbles = os.fspath(solid_dir / 'hands-bubbles.svg')
  
    file_circle_check = os.fspath(solid_dir / 'file-circle-check.svg')
  
    thermometer = os.fspath(solid_dir / 'thermometer.svg')
  
    brain = os.fspath(solid_dir / 'brain.svg')
  
    fish = os.fspath(solid_dir / 'fish.svg')
  
    plane = os.fspath(solid_dir / 'plane.svg')
  
    building_un = os.fspath(solid_dir / 'building-un.svg')
  
    mars_and_venus = os.fspath(solid_dir / 'mars-and-venus.svg')
  
    kiwi_bird = os.fspath(solid_dir / 'kiwi-bird.svg')
  
    face_grin_tongue = os.fspath(solid_dir / 'face-grin-tongue.svg')
  
    chart_area = os.fspath(solid_dir / 'chart-area.svg')
  
    laptop_code = os.fspath(solid_dir / 'laptop-code.svg')
  
    broom = os.fspath(solid_dir / 'broom.svg')
  
    torii_gate = os.fspath(solid_dir / 'torii-gate.svg')
  
    file_circle_xmark = os.fspath(solid_dir / 'file-circle-xmark.svg')
  
    fax = os.fspath(solid_dir / 'fax.svg')
  
    square_rss = os.fspath(solid_dir / 'square-rss.svg')
  
    align_right = os.fspath(solid_dir / 'align-right.svg')
  
    layer_group = os.fspath(solid_dir / 'layer-group.svg')
  
    masks_theater = os.fspath(solid_dir / 'masks-theater.svg')
  
    person_walking_arrow_loop_left = os.fspath(solid_dir / 'person-walking-arrow-loop-left.svg')
  
    cent_sign = os.fspath(solid_dir / 'cent-sign.svg')
  
    bottle_water = os.fspath(solid_dir / 'bottle-water.svg')
  
    restroom = os.fspath(solid_dir / 'restroom.svg')
  
    window_minimize = os.fspath(solid_dir / 'window-minimize.svg')
  
    bag_shopping = os.fspath(solid_dir / 'bag-shopping.svg')
  
    wave_square = os.fspath(solid_dir / 'wave-square.svg')
  
    money_bill_transfer = os.fspath(solid_dir / 'money-bill-transfer.svg')
  
    bangladeshi_taka_sign = os.fspath(solid_dir / 'bangladeshi-taka-sign.svg')
  
    earth_europe = os.fspath(solid_dir / 'earth-europe.svg')
  
    seedling = os.fspath(solid_dir / 'seedling.svg')
  
    computer = os.fspath(solid_dir / 'computer.svg')
  
    bath = os.fspath(solid_dir / 'bath.svg')
  
    baby = os.fspath(solid_dir / 'baby.svg')
  
    user_shield = os.fspath(solid_dir / 'user-shield.svg')
  
    tablet = os.fspath(solid_dir / 'tablet.svg')
  
    phone_volume = os.fspath(solid_dir / 'phone-volume.svg')
  
    pencil = os.fspath(solid_dir / 'pencil.svg')
  
    trash_arrow_up = os.fspath(solid_dir / 'trash-arrow-up.svg')
  
    thumbs_down = os.fspath(solid_dir / 'thumbs-down.svg')
  
    jet_fighter = os.fspath(solid_dir / 'jet-fighter.svg')
  
    drum_steelpan = os.fspath(solid_dir / 'drum-steelpan.svg')
  
    syringe = os.fspath(solid_dir / 'syringe.svg')
  
    synagogue = os.fspath(solid_dir / 'synagogue.svg')
  
    note_sticky = os.fspath(solid_dir / 'note-sticky.svg')
  
    file_excel = os.fspath(solid_dir / 'file-excel.svg')
  
    face_grin_tongue_squint = os.fspath(solid_dir / 'face-grin-tongue-squint.svg')
  
    exclamation = os.fspath(solid_dir / 'exclamation.svg')
  
    house_chimney_medical = os.fspath(solid_dir / 'house-chimney-medical.svg')
  
    bold = os.fspath(solid_dir / 'bold.svg')
  
    ellipsis = os.fspath(solid_dir / 'ellipsis.svg')
  
    file_powerpoint = os.fspath(solid_dir / 'file-powerpoint.svg')
  
    superscript = os.fspath(solid_dir / 'superscript.svg')
  
    arrow_trend_down = os.fspath(solid_dir / 'arrow-trend-down.svg')
  
    paper_plane = os.fspath(solid_dir / 'paper-plane.svg')
  
    train = os.fspath(solid_dir / 'train.svg')
  
    binoculars = os.fspath(solid_dir / 'binoculars.svg')
  
    diamond_turn_right = os.fspath(solid_dir / 'diamond-turn-right.svg')
  
    person_walking_with_cane = os.fspath(solid_dir / 'person-walking-with-cane.svg')
  
    eraser = os.fspath(solid_dir / 'eraser.svg')
  
    pager = os.fspath(solid_dir / 'pager.svg')
  
    mosquito = os.fspath(solid_dir / 'mosquito.svg')
  
    code_merge = os.fspath(solid_dir / 'code-merge.svg')
  
    o = os.fspath(solid_dir / 'o.svg')
  
    cubes = os.fspath(solid_dir / 'cubes.svg')
  
    burst = os.fspath(solid_dir / 'burst.svg')
  
    outdent = os.fspath(solid_dir / 'outdent.svg')
  
    i = os.fspath(solid_dir / 'i.svg')
  
    rainbow = os.fspath(solid_dir / 'rainbow.svg')
  
    circle_chevron_left = os.fspath(solid_dir / 'circle-chevron-left.svg')
  
    virus_slash = os.fspath(solid_dir / 'virus-slash.svg')
  
    marker = os.fspath(solid_dir / 'marker.svg')
  
    code_fork = os.fspath(solid_dir / 'code-fork.svg')
  
    arrow_down_1_9 = os.fspath(solid_dir / 'arrow-down-1-9.svg')
  
    trash = os.fspath(solid_dir / 'trash.svg')
  
    arrows_down_to_people = os.fspath(solid_dir / 'arrows-down-to-people.svg')
  
    egg = os.fspath(solid_dir / 'egg.svg')
  
    f = os.fspath(solid_dir / 'f.svg')
  
    mobile_screen = os.fspath(solid_dir / 'mobile-screen.svg')
  
    people_carry_box = os.fspath(solid_dir / 'people-carry-box.svg')
  
    face_meh = os.fspath(solid_dir / 'face-meh.svg')
  
    pen_to_square = os.fspath(solid_dir / 'pen-to-square.svg')
  
    dove = os.fspath(solid_dir / 'dove.svg')
  
    gauge_simple = os.fspath(solid_dir / 'gauge-simple.svg')
  
    cloud_showers_heavy = os.fspath(solid_dir / 'cloud-showers-heavy.svg')
  
    suitcase_rolling = os.fspath(solid_dir / 'suitcase-rolling.svg')
  
    spoon = os.fspath(solid_dir / 'spoon.svg')
  
    clipboard_question = os.fspath(solid_dir / 'clipboard-question.svg')
  
    face_sad_tear = os.fspath(solid_dir / 'face-sad-tear.svg')
  
    person_skiing_nordic = os.fspath(solid_dir / 'person-skiing-nordic.svg')
  
    person_hiking = os.fspath(solid_dir / 'person-hiking.svg')
  
    ranking_star = os.fspath(solid_dir / 'ranking-star.svg')
  
    ankh = os.fspath(solid_dir / 'ankh.svg')
  
    battery_half = os.fspath(solid_dir / 'battery-half.svg')
  
    square_caret_down = os.fspath(solid_dir / 'square-caret-down.svg')
  
    trash_can = os.fspath(solid_dir / 'trash-can.svg')
  
    hand = os.fspath(solid_dir / 'hand.svg')
  
    square_arrow_up_right = os.fspath(solid_dir / 'square-arrow-up-right.svg')
  
    children = os.fspath(solid_dir / 'children.svg')
  
    tape = os.fspath(solid_dir / 'tape.svg')
  
    face_tired = os.fspath(solid_dir / 'face-tired.svg')
  
    _5 = os.fspath(solid_dir / '5.svg')
  
    shield_cat = os.fspath(solid_dir / 'shield-cat.svg')
  
    scroll = os.fspath(solid_dir / 'scroll.svg')
  
    rotate = os.fspath(solid_dir / 'rotate.svg')
  
    house_circle_check = os.fspath(solid_dir / 'house-circle-check.svg')
  
    mitten = os.fspath(solid_dir / 'mitten.svg')
  
    right_to_bracket = os.fspath(solid_dir / 'right-to-bracket.svg')
  
    rug = os.fspath(solid_dir / 'rug.svg')
  
    spray_can = os.fspath(solid_dir / 'spray-can.svg')
  
    book = os.fspath(solid_dir / 'book.svg')
  
    hill_avalanche = os.fspath(solid_dir / 'hill-avalanche.svg')
  
    rectangle_ad = os.fspath(solid_dir / 'rectangle-ad.svg')
  
    face_grin_wide = os.fspath(solid_dir / 'face-grin-wide.svg')
  
    wallet = os.fspath(solid_dir / 'wallet.svg')
  
    house_flag = os.fspath(solid_dir / 'house-flag.svg')
  
    c = os.fspath(solid_dir / 'c.svg')
  
    angles_right = os.fspath(solid_dir / 'angles-right.svg')
  
    dollar_sign = os.fspath(solid_dir / 'dollar-sign.svg')
  
    s = os.fspath(solid_dir / 's.svg')
  
    boxes_stacked = os.fspath(solid_dir / 'boxes-stacked.svg')
  
    graduation_cap = os.fspath(solid_dir / 'graduation-cap.svg')
  
    utensils = os.fspath(solid_dir / 'utensils.svg')
  
    hand_holding_dollar = os.fspath(solid_dir / 'hand-holding-dollar.svg')
  
    copy = os.fspath(solid_dir / 'copy.svg')
  
    spinner = os.fspath(solid_dir / 'spinner.svg')
  
    building_user = os.fspath(solid_dir / 'building-user.svg')
  
    teeth_open = os.fspath(solid_dir / 'teeth-open.svg')
  
    house_medical_circle_exclamation = os.fspath(solid_dir / 'house-medical-circle-exclamation.svg')
  
    broom_ball = os.fspath(solid_dir / 'broom-ball.svg')
  
    bridge_lock = os.fspath(solid_dir / 'bridge-lock.svg')
  
    tty = os.fspath(solid_dir / 'tty.svg')
  
    building_columns = os.fspath(solid_dir / 'building-columns.svg')
  
    reply = os.fspath(solid_dir / 'reply.svg')
  
    terminal = os.fspath(solid_dir / 'terminal.svg')
  
    handshake_angle = os.fspath(solid_dir / 'handshake-angle.svg')
  
    down_long = os.fspath(solid_dir / 'down-long.svg')
  
    peseta_sign = os.fspath(solid_dir / 'peseta-sign.svg')
  
    house_medical_flag = os.fspath(solid_dir / 'house-medical-flag.svg')
  
    calendar = os.fspath(solid_dir / 'calendar.svg')
  
    gifts = os.fspath(solid_dir / 'gifts.svg')
  
    face_flushed = os.fspath(solid_dir / 'face-flushed.svg')
  
    circle_xmark = os.fspath(solid_dir / 'circle-xmark.svg')
  
    wine_glass = os.fspath(solid_dir / 'wine-glass.svg')
  
    lungs_virus = os.fspath(solid_dir / 'lungs-virus.svg')
  
    crop = os.fspath(solid_dir / 'crop.svg')
  
    dumpster = os.fspath(solid_dir / 'dumpster.svg')
  
    book_bookmark = os.fspath(solid_dir / 'book-bookmark.svg')
  
    cruzeiro_sign = os.fspath(solid_dir / 'cruzeiro-sign.svg')
  
    house_lock = os.fspath(solid_dir / 'house-lock.svg')
  
    tree = os.fspath(solid_dir / 'tree.svg')
  
    face_smile = os.fspath(solid_dir / 'face-smile.svg')
  
    border_all = os.fspath(solid_dir / 'border-all.svg')
  
    church = os.fspath(solid_dir / 'church.svg')
  
    desktop = os.fspath(solid_dir / 'desktop.svg')
  
    chess_bishop = os.fspath(solid_dir / 'chess-bishop.svg')
  
    handshake_simple_slash = os.fspath(solid_dir / 'handshake-simple-slash.svg')
  
    virus_covid_slash = os.fspath(solid_dir / 'virus-covid-slash.svg')
  
    person_biking = os.fspath(solid_dir / 'person-biking.svg')
  
    book_journal_whills = os.fspath(solid_dir / 'book-journal-whills.svg')
  
    mountain_city = os.fspath(solid_dir / 'mountain-city.svg')
  
    star_half_stroke = os.fspath(solid_dir / 'star-half-stroke.svg')
  
    temperature_high = os.fspath(solid_dir / 'temperature-high.svg')
  
    _6 = os.fspath(solid_dir / '6.svg')
  
    brush = os.fspath(solid_dir / 'brush.svg')
  
    users_gear = os.fspath(solid_dir / 'users-gear.svg')
  
    magnifying_glass_arrow_right = os.fspath(solid_dir / 'magnifying-glass-arrow-right.svg')
  
    helmet_safety = os.fspath(solid_dir / 'helmet-safety.svg')
  
    hand_holding_medical = os.fspath(solid_dir / 'hand-holding-medical.svg')
  
    hat_cowboy_side = os.fspath(solid_dir / 'hat-cowboy-side.svg')
  
    maximize = os.fspath(solid_dir / 'maximize.svg')
  
    cake_candles = os.fspath(solid_dir / 'cake-candles.svg')
  
    face_grin_wink = os.fspath(solid_dir / 'face-grin-wink.svg')
  
    tent_arrow_left_right = os.fspath(solid_dir / 'tent-arrow-left-right.svg')
  
    envelopes_bulk = os.fspath(solid_dir / 'envelopes-bulk.svg')
  
    arrows_turn_to_dots = os.fspath(solid_dir / 'arrows-turn-to-dots.svg')
  
    person_swimming = os.fspath(solid_dir / 'person-swimming.svg')
  
    lock = os.fspath(solid_dir / 'lock.svg')
  
    cloud_meatball = os.fspath(solid_dir / 'cloud-meatball.svg')
  
    temperature_empty = os.fspath(solid_dir / 'temperature-empty.svg')
  
    sign_hanging = os.fspath(solid_dir / 'sign-hanging.svg')
  
    _2 = os.fspath(solid_dir / '2.svg')
  
    toilet_portable = os.fspath(solid_dir / 'toilet-portable.svg')
  
    trophy = os.fspath(solid_dir / 'trophy.svg')
  
    face_sad_cry = os.fspath(solid_dir / 'face-sad-cry.svg')
  
    ghost = os.fspath(solid_dir / 'ghost.svg')
  
    file_lines = os.fspath(solid_dir / 'file-lines.svg')
  
    dice_six = os.fspath(solid_dir / 'dice-six.svg')
  
    face_grin_squint_tears = os.fspath(solid_dir / 'face-grin-squint-tears.svg')
  
    hands_asl_interpreting = os.fspath(solid_dir / 'hands-asl-interpreting.svg')
  
    naira_sign = os.fspath(solid_dir / 'naira-sign.svg')
  
    hands_holding_child = os.fspath(solid_dir / 'hands-holding-child.svg')
  
    cart_plus = os.fspath(solid_dir / 'cart-plus.svg')
  
    circle_nodes = os.fspath(solid_dir / 'circle-nodes.svg')
  
    arrow_turn_down = os.fspath(solid_dir / 'arrow-turn-down.svg')
  
    microchip = os.fspath(solid_dir / 'microchip.svg')
  
    cow = os.fspath(solid_dir / 'cow.svg')
  
    hand_point_right = os.fspath(solid_dir / 'hand-point-right.svg')
  
    crown = os.fspath(solid_dir / 'crown.svg')
  
    wifi = os.fspath(solid_dir / 'wifi.svg')
  
    arrows_rotate = os.fspath(solid_dir / 'arrows-rotate.svg')
  
    plus_minus = os.fspath(solid_dir / 'plus-minus.svg')
  
    b = os.fspath(solid_dir / 'b.svg')
  
    filter_circle_dollar = os.fspath(solid_dir / 'filter-circle-dollar.svg')
  
    volume_low = os.fspath(solid_dir / 'volume-low.svg')
  
    caret_down = os.fspath(solid_dir / 'caret-down.svg')
  
    sitemap = os.fspath(solid_dir / 'sitemap.svg')
  
    transgender = os.fspath(solid_dir / 'transgender.svg')
  
    vihara = os.fspath(solid_dir / 'vihara.svg')
  
    book_open_reader = os.fspath(solid_dir / 'book-open-reader.svg')
  
    square_root_variable = os.fspath(solid_dir / 'square-root-variable.svg')
  
    d = os.fspath(solid_dir / 'd.svg')
  
    house_medical_circle_xmark = os.fspath(solid_dir / 'house-medical-circle-xmark.svg')
  
    school_circle_exclamation = os.fspath(solid_dir / 'school-circle-exclamation.svg')
  
    greater_than_equal = os.fspath(solid_dir / 'greater-than-equal.svg')
  
    arrow_up_short_wide = os.fspath(solid_dir / 'arrow-up-short-wide.svg')
  
    car = os.fspath(solid_dir / 'car.svg')
  
    power_off = os.fspath(solid_dir / 'power-off.svg')
  
    truck = os.fspath(solid_dir / 'truck.svg')
  
    timeline = os.fspath(solid_dir / 'timeline.svg')
  
    h = os.fspath(solid_dir / 'h.svg')
  
    face_frown_open = os.fspath(solid_dir / 'face-frown-open.svg')
  
    mobile_retro = os.fspath(solid_dir / 'mobile-retro.svg')
  
    _4 = os.fspath(solid_dir / '4.svg')
  
    yen_sign = os.fspath(solid_dir / 'yen-sign.svg')
  
    image = os.fspath(solid_dir / 'image.svg')
  
    tower_cell = os.fspath(solid_dir / 'tower-cell.svg')
  
    jet_fighter_up = os.fspath(solid_dir / 'jet-fighter-up.svg')
  
    heart_crack = os.fspath(solid_dir / 'heart-crack.svg')
  
    staff_snake = os.fspath(solid_dir / 'staff-snake.svg')
  
    circle_minus = os.fspath(solid_dir / 'circle-minus.svg')
  
    chess_board = os.fspath(solid_dir / 'chess-board.svg')
  
    minimize = os.fspath(solid_dir / 'minimize.svg')
  
    person_chalkboard = os.fspath(solid_dir / 'person-chalkboard.svg')
  
    bucket = os.fspath(solid_dir / 'bucket.svg')
  
    bell_concierge = os.fspath(solid_dir / 'bell-concierge.svg')
  
    route = os.fspath(solid_dir / 'route.svg')
  
    circle_radiation = os.fspath(solid_dir / 'circle-radiation.svg')
  
    delete_left = os.fspath(solid_dir / 'delete-left.svg')
  
    hot_tub_person = os.fspath(solid_dir / 'hot-tub-person.svg')
  
    right_left = os.fspath(solid_dir / 'right-left.svg')
  
    users_rectangle = os.fspath(solid_dir / 'users-rectangle.svg')
  
    folder_open = os.fspath(solid_dir / 'folder-open.svg')
  
    folder_closed = os.fspath(solid_dir / 'folder-closed.svg')
  
    house_medical_circle_check = os.fspath(solid_dir / 'house-medical-circle-check.svg')
  
    shield_halved = os.fspath(solid_dir / 'shield-halved.svg')
  
    spider = os.fspath(solid_dir / 'spider.svg')
  
    building = os.fspath(solid_dir / 'building.svg')
  
    ticket = os.fspath(solid_dir / 'ticket.svg')
  
    crow = os.fspath(solid_dir / 'crow.svg')
  
    hourglass_end = os.fspath(solid_dir / 'hourglass-end.svg')
  
    message = os.fspath(solid_dir / 'message.svg')
  
    walkie_talkie = os.fspath(solid_dir / 'walkie-talkie.svg')
  
    khanda = os.fspath(solid_dir / 'khanda.svg')
  
    fire_flame_simple = os.fspath(solid_dir / 'fire-flame-simple.svg')
  
    road_barrier = os.fspath(solid_dir / 'road-barrier.svg')
  
    hotdog = os.fspath(solid_dir / 'hotdog.svg')
  
    pen_ruler = os.fspath(solid_dir / 'pen-ruler.svg')
  
    mars_stroke_right = os.fspath(solid_dir / 'mars-stroke-right.svg')
  
    highlighter = os.fspath(solid_dir / 'highlighter.svg')
  
    face_kiss = os.fspath(solid_dir / 'face-kiss.svg')
  
    object_ungroup = os.fspath(solid_dir / 'object-ungroup.svg')
  
    burger = os.fspath(solid_dir / 'burger.svg')
  
    hands_holding_circle = os.fspath(solid_dir / 'hands-holding-circle.svg')
  
    dungeon = os.fspath(solid_dir / 'dungeon.svg')
  
    star_of_david = os.fspath(solid_dir / 'star-of-david.svg')
  
    carrot = os.fspath(solid_dir / 'carrot.svg')
  
    square_caret_left = os.fspath(solid_dir / 'square-caret-left.svg')
  
    square_caret_up = os.fspath(solid_dir / 'square-caret-up.svg')
  
    boxes_packing = os.fspath(solid_dir / 'boxes-packing.svg')
  
    hand_lizard = os.fspath(solid_dir / 'hand-lizard.svg')
  
    code = os.fspath(solid_dir / 'code.svg')
  
    coins = os.fspath(solid_dir / 'coins.svg')
  
    plane_up = os.fspath(solid_dir / 'plane-up.svg')
  
    bug_slash = os.fspath(solid_dir / 'bug-slash.svg')
  
    truck_monster = os.fspath(solid_dir / 'truck-monster.svg')
  
    key = os.fspath(solid_dir / 'key.svg')
  
    mobile_screen_button = os.fspath(solid_dir / 'mobile-screen-button.svg')
  
    indian_rupee_sign = os.fspath(solid_dir / 'indian-rupee-sign.svg')
  
    filter_circle_xmark = os.fspath(solid_dir / 'filter-circle-xmark.svg')
  
    user_large_slash = os.fspath(solid_dir / 'user-large-slash.svg')
  
    arrow_down_wide_short = os.fspath(solid_dir / 'arrow-down-wide-short.svg')
  
    face_meh_blank = os.fspath(solid_dir / 'face-meh-blank.svg')
  
    arrows_to_eye = os.fspath(solid_dir / 'arrows-to-eye.svg')
  
    toggle_off = os.fspath(solid_dir / 'toggle-off.svg')
  
    person_military_pointing = os.fspath(solid_dir / 'person-military-pointing.svg')
  
    folder_minus = os.fspath(solid_dir / 'folder-minus.svg')
  
    arrow_right_to_city = os.fspath(solid_dir / 'arrow-right-to-city.svg')
  
    square_virus = os.fspath(solid_dir / 'square-virus.svg')
  
    school = os.fspath(solid_dir / 'school.svg')
  
    backward_step = os.fspath(solid_dir / 'backward-step.svg')
  
    square_up_right = os.fspath(solid_dir / 'square-up-right.svg')
  
    bridge_circle_check = os.fspath(solid_dir / 'bridge-circle-check.svg')
  
    building_shield = os.fspath(solid_dir / 'building-shield.svg')
  
    j = os.fspath(solid_dir / 'j.svg')
  
    traffic_light = os.fspath(solid_dir / 'traffic-light.svg')
  
    clock_rotate_left = os.fspath(solid_dir / 'clock-rotate-left.svg')
  
    person_skiing = os.fspath(solid_dir / 'person-skiing.svg')
  
    hand_fist = os.fspath(solid_dir / 'hand-fist.svg')
  
    hands_holding = os.fspath(solid_dir / 'hands-holding.svg')
  
    file_invoice_dollar = os.fspath(solid_dir / 'file-invoice-dollar.svg')
  
    cart_flatbed_suitcase = os.fspath(solid_dir / 'cart-flatbed-suitcase.svg')
  
    file = os.fspath(solid_dir / 'file.svg')
  
    candy_cane = os.fspath(solid_dir / 'candy-cane.svg')
  
    comment = os.fspath(solid_dir / 'comment.svg')
  
    caret_right = os.fspath(solid_dir / 'caret-right.svg')
  
    oil_well = os.fspath(solid_dir / 'oil-well.svg')
  
    truck_fast = os.fspath(solid_dir / 'truck-fast.svg')
  
    border_top_left = os.fspath(solid_dir / 'border-top-left.svg')
  
    car_rear = os.fspath(solid_dir / 'car-rear.svg')
  
    toolbox = os.fspath(solid_dir / 'toolbox.svg')
  
    play = os.fspath(solid_dir / 'play.svg')
  
    turn_down = os.fspath(solid_dir / 'turn-down.svg')
  
    building_circle_check = os.fspath(solid_dir / 'building-circle-check.svg')
  
    dumbbell = os.fspath(solid_dir / 'dumbbell.svg')
  
    paintbrush = os.fspath(solid_dir / 'paintbrush.svg')
  
    lines_leaning = os.fspath(solid_dir / 'lines-leaning.svg')
  
    gamepad = os.fspath(solid_dir / 'gamepad.svg')
  
    ellipsis_vertical = os.fspath(solid_dir / 'ellipsis-vertical.svg')
  
    republican = os.fspath(solid_dir / 'republican.svg')
  
    x_ray = os.fspath(solid_dir / 'x-ray.svg')
  
    bell = os.fspath(solid_dir / 'bell.svg')
  
    earth_americas = os.fspath(solid_dir / 'earth-americas.svg')
  
    wheat_awn = os.fspath(solid_dir / 'wheat-awn.svg')
  
    jar = os.fspath(solid_dir / 'jar.svg')
  
    rupee_sign = os.fspath(solid_dir / 'rupee-sign.svg')
  
    hand_dots = os.fspath(solid_dir / 'hand-dots.svg')
  
    compass = os.fspath(solid_dir / 'compass.svg')
  
    pen_nib = os.fspath(solid_dir / 'pen-nib.svg')
  
    arrows_to_circle = os.fspath(solid_dir / 'arrows-to-circle.svg')
  
    grip = os.fspath(solid_dir / 'grip.svg')
  
    cloud_sun_rain = os.fspath(solid_dir / 'cloud-sun-rain.svg')
  
    store_slash = os.fspath(solid_dir / 'store-slash.svg')
  
    circle = os.fspath(solid_dir / 'circle.svg')
  
    lock_open = os.fspath(solid_dir / 'lock-open.svg')
  
    share = os.fspath(solid_dir / 'share.svg')
  
    dharmachakra = os.fspath(solid_dir / 'dharmachakra.svg')
  
    stopwatch = os.fspath(solid_dir / 'stopwatch.svg')
  
    glass_water = os.fspath(solid_dir / 'glass-water.svg')
  
    person_circle_plus = os.fspath(solid_dir / 'person-circle-plus.svg')
  
    passport = os.fspath(solid_dir / 'passport.svg')
  
    futbol = os.fspath(solid_dir / 'futbol.svg')
  
    robot = os.fspath(solid_dir / 'robot.svg')
  
    ruler = os.fspath(solid_dir / 'ruler.svg')
  
    kip_sign = os.fspath(solid_dir / 'kip-sign.svg')
  
    money_bills = os.fspath(solid_dir / 'money-bills.svg')
  
    won_sign = os.fspath(solid_dir / 'won-sign.svg')
  
    not_equal = os.fspath(solid_dir / 'not-equal.svg')
  
    repeat = os.fspath(solid_dir / 'repeat.svg')
  
    dice_one = os.fspath(solid_dir / 'dice-one.svg')
  
    square_check = os.fspath(solid_dir / 'square-check.svg')
  
    face_surprise = os.fspath(solid_dir / 'face-surprise.svg')
  
    snowflake = os.fspath(solid_dir / 'snowflake.svg')
  
    table_cells_large = os.fspath(solid_dir / 'table-cells-large.svg')
  
    bed = os.fspath(solid_dir / 'bed.svg')
  
    temperature_quarter = os.fspath(solid_dir / 'temperature-quarter.svg')
  
    arrow_up_right_dots = os.fspath(solid_dir / 'arrow-up-right-dots.svg')
  
    file_circle_question = os.fspath(solid_dir / 'file-circle-question.svg')
  
    road_circle_exclamation = os.fspath(solid_dir / 'road-circle-exclamation.svg')
  
    wheelchair_move = os.fspath(solid_dir / 'wheelchair-move.svg')
  
    circle_chevron_down = os.fspath(solid_dir / 'circle-chevron-down.svg')
  
    table_columns = os.fspath(solid_dir / 'table-columns.svg')
  
    volume_xmark = os.fspath(solid_dir / 'volume-xmark.svg')
  
    users_line = os.fspath(solid_dir / 'users-line.svg')
  
    bullhorn = os.fspath(solid_dir / 'bullhorn.svg')
  
    face_grin_beam_sweat = os.fspath(solid_dir / 'face-grin-beam-sweat.svg')
  
    gun = os.fspath(solid_dir / 'gun.svg')
  
    square_pen = os.fspath(solid_dir / 'square-pen.svg')
  
    smoking = os.fspath(solid_dir / 'smoking.svg')
  
    plug_circle_minus = os.fspath(solid_dir / 'plug-circle-minus.svg')
  
    map_location = os.fspath(solid_dir / 'map-location.svg')
  
    trailer = os.fspath(solid_dir / 'trailer.svg')
  
    radiation = os.fspath(solid_dir / 'radiation.svg')
  
    cloud_moon_rain = os.fspath(solid_dir / 'cloud-moon-rain.svg')
  
    user_tie = os.fspath(solid_dir / 'user-tie.svg')
  
    sort_up = os.fspath(solid_dir / 'sort-up.svg')
  
    turn_up = os.fspath(solid_dir / 'turn-up.svg')
  
    images = os.fspath(solid_dir / 'images.svg')
  
    circle_question = os.fspath(solid_dir / 'circle-question.svg')
  
    child = os.fspath(solid_dir / 'child.svg')
  
    arrow_down_9_1 = os.fspath(solid_dir / 'arrow-down-9-1.svg')
  
    face_frown = os.fspath(solid_dir / 'face-frown.svg')
  
    signs_post = os.fspath(solid_dir / 'signs-post.svg')
  
    user_injured = os.fspath(solid_dir / 'user-injured.svg')
  
    file_image = os.fspath(solid_dir / 'file-image.svg')
  
    bed_pulse = os.fspath(solid_dir / 'bed-pulse.svg')
  
    monument = os.fspath(solid_dir / 'monument.svg')
  
    location_dot = os.fspath(solid_dir / 'location-dot.svg')
  
    person_digging = os.fspath(solid_dir / 'person-digging.svg')
  
    martini_glass_citrus = os.fspath(solid_dir / 'martini-glass-citrus.svg')
  
    map = os.fspath(solid_dir / 'map.svg')
  
    closed_captioning = os.fspath(solid_dir / 'closed-captioning.svg')
  
    font_awesome = os.fspath(solid_dir / 'font-awesome.svg')
  
    school_circle_xmark = os.fspath(solid_dir / 'school-circle-xmark.svg')
  
    file_waveform = os.fspath(solid_dir / 'file-waveform.svg')
  
    diagram_successor = os.fspath(solid_dir / 'diagram-successor.svg')
  
    file_medical = os.fspath(solid_dir / 'file-medical.svg')
  
    arrows_down_to_line = os.fspath(solid_dir / 'arrows-down-to-line.svg')
  
    hammer = os.fspath(solid_dir / 'hammer.svg')
  
    sack_dollar = os.fspath(solid_dir / 'sack-dollar.svg')
  
    hand_back_fist = os.fspath(solid_dir / 'hand-back-fist.svg')
  
    shuttle_space = os.fspath(solid_dir / 'shuttle-space.svg')
  
    holly_berry = os.fspath(solid_dir / 'holly-berry.svg')
  
    pause = os.fspath(solid_dir / 'pause.svg')
  
    weight_hanging = os.fspath(solid_dir / 'weight-hanging.svg')
  
    person_dress_burst = os.fspath(solid_dir / 'person-dress-burst.svg')
  
    person_pregnant = os.fspath(solid_dir / 'person-pregnant.svg')
  
    yin_yang = os.fspath(solid_dir / 'yin-yang.svg')
  
    screwdriver = os.fspath(solid_dir / 'screwdriver.svg')
  
    house = os.fspath(solid_dir / 'house.svg')
  
    circle_arrow_right = os.fspath(solid_dir / 'circle-arrow-right.svg')
  
    tarp_droplet = os.fspath(solid_dir / 'tarp-droplet.svg')
  
    person_drowning = os.fspath(solid_dir / 'person-drowning.svg')
  
    sun_plant_wilt = os.fspath(solid_dir / 'sun-plant-wilt.svg')
  
    arrow_up_long = os.fspath(solid_dir / 'arrow-up-long.svg')
  
    registered = os.fspath(solid_dir / 'registered.svg')
  
    xmarks_lines = os.fspath(solid_dir / 'xmarks-lines.svg')
  
    arrow_trend_up = os.fspath(solid_dir / 'arrow-trend-up.svg')
  
    cloud_arrow_up = os.fspath(solid_dir / 'cloud-arrow-up.svg')
  
    comment_slash = os.fspath(solid_dir / 'comment-slash.svg')
  
    circle_h = os.fspath(solid_dir / 'circle-h.svg')
  
    mosque = os.fspath(solid_dir / 'mosque.svg')
  
    sim_card = os.fspath(solid_dir / 'sim-card.svg')
  
    basket_shopping = os.fspath(solid_dir / 'basket-shopping.svg')
  
    chart_bar = os.fspath(solid_dir / 'chart-bar.svg')
  
    baby_carriage = os.fspath(solid_dir / 'baby-carriage.svg')
  
    circle_chevron_up = os.fspath(solid_dir / 'circle-chevron-up.svg')
  
    landmark = os.fspath(solid_dir / 'landmark.svg')
  
    screwdriver_wrench = os.fspath(solid_dir / 'screwdriver-wrench.svg')
  
    place_of_worship = os.fspath(solid_dir / 'place-of-worship.svg')
  
    file_signature = os.fspath(solid_dir / 'file-signature.svg')
  
    piggy_bank = os.fspath(solid_dir / 'piggy-bank.svg')
  
    chevron_up = os.fspath(solid_dir / 'chevron-up.svg')
  
    blender = os.fspath(solid_dir / 'blender.svg')
  
    truck_arrow_right = os.fspath(solid_dir / 'truck-arrow-right.svg')
  
    taxi = os.fspath(solid_dir / 'taxi.svg')
  
    subscript = os.fspath(solid_dir / 'subscript.svg')
  
    print = os.fspath(solid_dir / 'print.svg')
  
    clover = os.fspath(solid_dir / 'clover.svg')
  
    car_burst = os.fspath(solid_dir / 'car-burst.svg')
  
    shop = os.fspath(solid_dir / 'shop.svg')
  
    file_arrow_up = os.fspath(solid_dir / 'file-arrow-up.svg')
  
    umbrella = os.fspath(solid_dir / 'umbrella.svg')
  
    file_code = os.fspath(solid_dir / 'file-code.svg')
  
    mug_hot = os.fspath(solid_dir / 'mug-hot.svg')
  
    notdef = os.fspath(solid_dir / 'notdef.svg')
  
    bars = os.fspath(solid_dir / 'bars.svg')
  
    spell_check = os.fspath(solid_dir / 'spell-check.svg')
  
    venus_mars = os.fspath(solid_dir / 'venus-mars.svg')
  
    lemon = os.fspath(solid_dir / 'lemon.svg')
  
    microphone_lines_slash = os.fspath(solid_dir / 'microphone-lines-slash.svg')
  
    cloud = os.fspath(solid_dir / 'cloud.svg')
  
    umbrella_beach = os.fspath(solid_dir / 'umbrella-beach.svg')
  
    chess_knight = os.fspath(solid_dir / 'chess-knight.svg')
  
    cloud_bolt = os.fspath(solid_dir / 'cloud-bolt.svg')
  
    ruler_combined = os.fspath(solid_dir / 'ruler-combined.svg')
  
    arrow_down = os.fspath(solid_dir / 'arrow-down.svg')
  
    volleyball = os.fspath(solid_dir / 'volleyball.svg')
  
    file_arrow_down = os.fspath(solid_dir / 'file-arrow-down.svg')
  
    trowel = os.fspath(solid_dir / 'trowel.svg')
  
    house_chimney_window = os.fspath(solid_dir / 'house-chimney-window.svg')
  
    wand_sparkles = os.fspath(solid_dir / 'wand-sparkles.svg')
  
    chalkboard = os.fspath(solid_dir / 'chalkboard.svg')
  
    bugs = os.fspath(solid_dir / 'bugs.svg')
  
    group_arrows_rotate = os.fspath(solid_dir / 'group-arrows-rotate.svg')
  
    head_side_virus = os.fspath(solid_dir / 'head-side-virus.svg')
  
    paint_roller = os.fspath(solid_dir / 'paint-roller.svg')
  
    rectangle_list = os.fspath(solid_dir / 'rectangle-list.svg')
  
    bolt_lightning = os.fspath(solid_dir / 'bolt-lightning.svg')
  
    bandage = os.fspath(solid_dir / 'bandage.svg')
  
    magnifying_glass_plus = os.fspath(solid_dir / 'magnifying-glass-plus.svg')
  
    object_group = os.fspath(solid_dir / 'object-group.svg')
  
    strikethrough = os.fspath(solid_dir / 'strikethrough.svg')
  
    hand_point_down = os.fspath(solid_dir / 'hand-point-down.svg')
  
    square_envelope = os.fspath(solid_dir / 'square-envelope.svg')
  
    diagram_predecessor = os.fspath(solid_dir / 'diagram-predecessor.svg')
  
    cube = os.fspath(solid_dir / 'cube.svg')
  
    user_ninja = os.fspath(solid_dir / 'user-ninja.svg')
  
    quote_left = os.fspath(solid_dir / 'quote-left.svg')
  
    g = os.fspath(solid_dir / 'g.svg')
  
    car_on = os.fspath(solid_dir / 'car-on.svg')
  
    code_branch = os.fspath(solid_dir / 'code-branch.svg')
  
    check_to_slot = os.fspath(solid_dir / 'check-to-slot.svg')
  
    tarp = os.fspath(solid_dir / 'tarp.svg')
  
    l = os.fspath(solid_dir / 'l.svg')
  
    heart = os.fspath(solid_dir / 'heart.svg')
  
    fill_drip = os.fspath(solid_dir / 'fill-drip.svg')
  
    kit_medical = os.fspath(solid_dir / 'kit-medical.svg')
  
    door_closed = os.fspath(solid_dir / 'door-closed.svg')
  
    magnifying_glass_chart = os.fspath(solid_dir / 'magnifying-glass-chart.svg')
  
    toilet_paper_slash = os.fspath(solid_dir / 'toilet-paper-slash.svg')
  
    skull_crossbones = os.fspath(solid_dir / 'skull-crossbones.svg')
  
    signature = os.fspath(solid_dir / 'signature.svg')
  
    toilets_portable = os.fspath(solid_dir / 'toilets-portable.svg')
  
    hand_spock = os.fspath(solid_dir / 'hand-spock.svg')
  
    prescription = os.fspath(solid_dir / 'prescription.svg')
  
    people_arrows = os.fspath(solid_dir / 'people-arrows.svg')
  
    road_circle_xmark = os.fspath(solid_dir / 'road-circle-xmark.svg')
  
    feather_pointed = os.fspath(solid_dir / 'feather-pointed.svg')
  
    peace = os.fspath(solid_dir / 'peace.svg')
  
    car_tunnel = os.fspath(solid_dir / 'car-tunnel.svg')
  
    arrow_rotate_right = os.fspath(solid_dir / 'arrow-rotate-right.svg')
  
    people_pulling = os.fspath(solid_dir / 'people-pulling.svg')
  


def _get_svg_object(fp: str):
    color = BLACK
    if str(config.background_color) == 'black':
        color = WHITE
    return SVGMobject(fp, color=color)


class Brand:
    """Brand SVG files defined in font-awesome/svgs/brands"""
    def __init__(self) -> None:
        pass

    def __getattr__(self, name) -> SVGMobject:
        return _get_svg_object(_Brand.__members__[name].value)


class Regular:
    """Regular SVG files defined in font-awesome/svgs/regular"""
    def __init__(self) -> None:
        pass

    def __getattr__(self, name) -> SVGMobject:
        return _get_svg_object(_Regular.__members__[name].value)


class Solid:
    """Solid SVG files defined in font-awesome/svgs/solid"""
    def __init__(self) -> None:
        pass

    def __getattr__(self, name) -> SVGMobject:
        return _get_svg_object(_Solid.__members__[name].value)


brand = Brand()
regular = Regular()
solid = Solid()