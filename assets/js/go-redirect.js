(function () {
  var targetMeta = document.querySelector('meta[name="redirect-target"]');
  if (!targetMeta) {
    return;
  }

  var partner = (document.querySelector('meta[name="redirect-partner"]') || {}).content || "unknown";
  var slug = (document.querySelector('meta[name="redirect-slug"]') || {}).content || window.location.pathname;
  var targetRaw = targetMeta.content;
  var statusNode = document.querySelector("[data-redirect-status]");
  var fallbackLink = document.querySelector("[data-redirect-fallback]");

  function buildTrackedUrl(rawUrl) {
    try {
      var url = new URL(rawUrl);
      if (!url.searchParams.has("utm_source")) url.searchParams.set("utm_source", "khloegrace.com");
      if (!url.searchParams.has("utm_medium")) url.searchParams.set("utm_medium", "referral");
      if (!url.searchParams.has("utm_campaign")) url.searchParams.set("utm_campaign", "official_channels");
      if (!url.searchParams.has("utm_content")) url.searchParams.set("utm_content", slug);
      return url.toString();
    } catch (err) {
      console.error("Error building tracked URL:", err);
      return rawUrl;
    }
  }

  function extractDomain(urlString) {
    try {
      return new URL(urlString).hostname;
    } catch (err) {
      console.error("Error extracting domain:", err);
      return "";
    }
  }

  var trackedTarget = buildTrackedUrl(targetRaw);

  if (fallbackLink) {
    fallbackLink.href = trackedTarget;
  }

  if (statusNode) {
    statusNode.textContent = "Redirecting to " + partner + "...";
  }

  function goNow() {
    try {
      window.location.replace(trackedTarget);
    } catch (err) {
      console.error("Error redirecting:", err);
      if (fallbackLink) {
        fallbackLink.click();
      }
    }
  }

  if (typeof window.gtag !== "function") {
    goNow();
    return;
  }

  var fired = false;
  function safeRedirect() {
    if (fired) {
      return;
    }
    fired = true;
    goNow();
  }

  try {
    window.gtag("event", "outbound_redirect", {
      event_category: "affiliate_tracking",
      event_label: partner,
      link_url: trackedTarget,
      link_domain: extractDomain(trackedTarget),
      redirect_slug: slug,
      transport_type: "beacon",
      event_callback: safeRedirect
    });
  } catch (err) {
    console.error("Error sending gtag event:", err);
    safeRedirect();
    return;
  }

  window.setTimeout(safeRedirect, 1500);
})();
