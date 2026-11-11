(function () {
  'use strict';

  const MANIFEST_URL = 'static/cad-build/manifest.json';
  const ASSET_ROOT = 'static/cad-build/';
  const MEDIA_REVISION = '20261008-rotation-60fps-1';
  const VIDEO_FPS = 60;
  const DEFAULT_STEP_DURATION = 2100;
  const FINAL_STEP_DURATION = 2800;
  const AUTO_ROTATION_PERIOD_MS = 8200;

  function assetUrl(value) {
    if (!value || typeof value !== 'string') return '';
    if (/^(?:https?:|data:|\/)/i.test(value) || value.startsWith('static/')) return value;
    if (value.startsWith('cad-build/')) return 'static/' + value;
    return ASSET_ROOT + value.replace(/^\.\//, '');
  }

  function mediaAssetUrl(value) {
    const url = assetUrl(value);
    if (!url) return '';
    if (window.location.protocol === 'file:') return url;
    return url + (url.includes('?') ? '&' : '?') + 'v=' + MEDIA_REVISION;
  }

  function bundledMesh(meshUrl) {
    const meshes = window.CAD_BUILD_MESHES;
    if (!meshes || !meshUrl) return null;
    const cleanUrl = String(meshUrl).split(/[?#]/, 1)[0].replace(/\\/g, '/');
    const marker = 'static/cad-build/';
    const markerIndex = cleanUrl.indexOf(marker);
    const key = markerIndex >= 0 ? cleanUrl.slice(markerIndex + marker.length) : cleanUrl.replace(/^\.\//, '');
    return Object.prototype.hasOwnProperty.call(meshes, key) ? meshes[key] : null;
  }

  function clamp(value, min, max) {
    return Math.min(max, Math.max(min, value));
  }

  function escapeHtml(value) {
    return String(value)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  function syntaxLine(line) {
    const keywords = new Set([
      'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue',
      'def', 'del', 'elif', 'else', 'except', 'False', 'finally', 'for',
      'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'None', 'nonlocal',
      'not', 'or', 'pass', 'raise', 'return', 'True', 'try', 'while', 'with', 'yield'
    ]);
    let html = '';
    let index = 0;

    while (index < line.length) {
      const char = line[index];

      if (char === '#') {
        html += '<span class="cad-token-comment">' + escapeHtml(line.slice(index)) + '</span>';
        break;
      }

      if (char === '"' || char === "'") {
        const quote = char;
        const triple = line.slice(index, index + 3) === quote.repeat(3);
        const markerLength = triple ? 3 : 1;
        let end = index + markerLength;
        while (end < line.length) {
          if (line[end] === '\\') {
            end += 2;
            continue;
          }
          if (line.slice(end, end + markerLength) === quote.repeat(markerLength)) {
            end += markerLength;
            break;
          }
          end += 1;
        }
        html += '<span class="cad-token-string">' + escapeHtml(line.slice(index, end)) + '</span>';
        index = end;
        continue;
      }

      if (/\d/.test(char) && (index === 0 || !/[A-Za-z_]/.test(line[index - 1]))) {
        const match = line.slice(index).match(/^\d+(?:\.\d+)?/);
        if (match) {
          html += '<span class="cad-token-number">' + match[0] + '</span>';
          index += match[0].length;
          continue;
        }
      }

      if (/[A-Za-z_]/.test(char)) {
        const match = line.slice(index).match(/^[A-Za-z_][A-Za-z0-9_]*/);
        const token = match ? match[0] : char;
        const remainder = line.slice(index + token.length);
        let className = '';
        if (keywords.has(token)) className = 'cad-token-keyword';
        else if (/^\s*\(/.test(remainder)) className = 'cad-token-call';
        html += className
          ? '<span class="' + className + '">' + escapeHtml(token) + '</span>'
          : escapeHtml(token);
        index += token.length;
        continue;
      }

      html += escapeHtml(char);
      index += 1;
    }

    return html || ' ';
  }

  function isEscaped(value, index) {
    let slashes = 0;
    for (let cursor = index - 1; cursor >= 0 && value[cursor] === '\\'; cursor -= 1) slashes += 1;
    return slashes % 2 === 1;
  }

  function findStringEnd(value, delimiter, start) {
    for (let index = start; index <= value.length - delimiter.length; index += 1) {
      if (value.slice(index, index + delimiter.length) === delimiter && !isEscaped(value, index)) return index;
    }
    return -1;
  }

  function removeStandaloneStrings(lines) {
    const output = [];
    let delimiter = '';
    let indentation = '';

    lines.forEach((line, index) => {
      let value = line;
      if (delimiter) {
        const end = findStringEnd(value, delimiter, 0);
        if (end < 0) return;
        value = indentation + value.slice(end + delimiter.length).replace(/^\s*;?\s*/, '');
        delimiter = '';
        indentation = '';
      }

      const match = value.match(/^(\s*)(?:[rubf]{0,2})?("""|''')/i);
      if (match) {
        const marker = match[2];
        const opening = match[0].length;
        const end = findStringEnd(value, marker, opening);
        if (end < 0) {
          delimiter = marker;
          indentation = match[1];
          return;
        }
        value = match[1] + value.slice(end + marker.length).replace(/^\s*;?\s*/, '');
      }

      output.push({ sourceLine: index + 1, text: value });
    });

    return output;
  }

  function removePythonComments(rows) {
    let delimiter = '';

    return rows.map((row) => {
      const value = row.text;
      let output = '';
      let index = 0;

      while (index < value.length) {
        if (delimiter) {
          const end = findStringEnd(value, delimiter, index);
          if (end < 0) {
            output += value.slice(index);
            index = value.length;
            continue;
          }
          output += value.slice(index, end + delimiter.length);
          index = end + delimiter.length;
          delimiter = '';
          continue;
        }

        const char = value[index];
        if (char === '#') break;
        if (char === '"' || char === "'") {
          const marker = value.slice(index, index + 3) === char.repeat(3) ? char.repeat(3) : char;
          const end = findStringEnd(value, marker, index + marker.length);
          if (end < 0) {
            output += value.slice(index);
            delimiter = marker;
            index = value.length;
            continue;
          }
          output += value.slice(index, end + marker.length);
          index = end + marker.length;
          continue;
        }

        output += char;
        index += 1;
      }

      return { sourceLine: row.sourceLine, text: output.replace(/\s+$/, '') };
    });
  }

  function prepareCodeForDisplay(source) {
    const lines = String(source || '').replace(/\r\n?/g, '\n').split('\n');
    return removePythonComments(removeStandaloneStrings(lines)).filter((row) => row.text.trim());
  }

  async function loadCode(part) {
    if (typeof part.sourceCode === 'string') return part.sourceCode;
    if (typeof part.code === 'string' && part.code.includes('\n')) return part.code;
    if (typeof part.source === 'string' && part.source.includes('\n')) return part.source;

    const path = part.codePath || part.codeFile || part.sourcePath || part.source || part.code;
    if (!path) return '';
    const response = await fetch(assetUrl(path));
    if (!response.ok) throw new Error('Unable to load ' + path + ' (' + response.status + ')');
    return response.text();
  }

  function normaliseFrame(frame) {
    if (typeof frame === 'string') return mediaAssetUrl(frame);
    if (frame && typeof frame === 'object') return mediaAssetUrl(frame.src || frame.path || frame.image);
    return '';
  }

  async function normalisePart(part, partIndex, manifestStepDuration) {
    const frames = (part.frames || part.stageFrames || part.images || []).map(normaliseFrame).filter(Boolean);
    const rawSteps = part.steps && part.steps.length ? part.steps : frames.map((frame, index) => ({
      label: 'Construction stage ' + (index + 1),
      frame: frame,
      frameIndex: index
    }));

    const steps = rawSteps.map((step, stepIndex) => {
      let frame = normaliseFrame(step.frame || step.image || step.src);
      const frameIndex = Number.isFinite(Number(step.frameIndex)) ? Number(step.frameIndex) : stepIndex;
      if (!frame) frame = frames[clamp(frameIndex, 0, Math.max(0, frames.length - 1))] || '';
      const startLine = Number(step.lineStart ?? step.startLine ?? step.lines?.[0] ?? 1);
      const endLine = Number(step.lineEnd ?? step.endLine ?? step.lines?.[1] ?? startLine);
      const configuredDuration = Number(
        step.durationMs ||
        step.duration ||
        part.defaultStepDurationMs ||
        manifestStepDuration ||
        DEFAULT_STEP_DURATION
      );
      const videoDuration = Math.max(
        1000 / VIDEO_FPS,
        Math.round((configuredDuration * VIDEO_FPS) / 1000) * (1000 / VIDEO_FPS)
      );
      return {
        label: step.label || step.name || step.operation || 'Construction stage ' + (stepIndex + 1),
        detail: step.detail || step.description || step.caption || 'Executing editable CadQuery operations',
        frame: frame,
        mesh: mediaAssetUrl(step.mesh || step.meshPath || step.geometry),
        lineStart: Math.max(1, startLine || 1),
        lineEnd: Math.max(1, endLine || startLine || 1),
        duration: Math.max(
          stepIndex === rawSteps.length - 1 ? 2300 : 1700,
          Number.isFinite(configuredDuration) ? configuredDuration : DEFAULT_STEP_DURATION
        ),
        videoDuration: Number.isFinite(videoDuration) ? videoDuration : DEFAULT_STEP_DURATION
      };
    });

    if (!steps.length) {
      steps.push({
        label: 'Final editable solid',
        detail: 'Parametric reconstruction complete',
        frame: frames[0] || normaliseFrame(part.preview || part.modelImage),
        lineStart: 1,
        lineEnd: 1,
        duration: FINAL_STEP_DURATION
      });
    }

    const remotion = part.remotion && part.remotion.animation ? {
      animation: mediaAssetUrl(part.remotion.animation),
      fps: Number(part.remotion.fps || VIDEO_FPS),
      durationMs: Number(part.remotion.durationMs || 0),
      finalHoldMs: Number(part.remotion.finalHoldMs || 1100)
    } : null;

    return {
      id: String(part.id || part.name || String(partIndex + 1).padStart(8, '0')),
      title: part.title || part.displayName || 'Mechanical component ' + String(partIndex + 1).padStart(2, '0'),
      drawing: assetUrl(part.drawing || part.drawingImage || part.blueprint),
      drawingType: part.drawingType || 'STANDARDIZED 2D INPUT',
      scale: part.scale || 'ISO / MM',
      codeFile: part.codeFileName || part.filename || (String(part.id || part.name || 'part') + '.py'),
      sourceCode: await loadCode(part),
      steps: steps,
      remotion: remotion,
      modelColor: part.modelColor || '#7996B3'
    };
  }

  function parseHexColor(value) {
    const match = /^#?([0-9a-f]{6})$/i.exec(String(value || ''));
    const hex = match ? match[1] : '7996B3';
    return [
      Number.parseInt(hex.slice(0, 2), 16) / 255,
      Number.parseInt(hex.slice(2, 4), 16) / 255,
      Number.parseInt(hex.slice(4, 6), 16) / 255
    ];
  }

  class CadMeshRenderer {
    constructor(canvas, viewport) {
      this.canvas = canvas;
      this.viewport = viewport;
      this.gl = canvas.getContext('webgl', {
        alpha: true,
        antialias: true,
        depth: true,
        premultipliedAlpha: true,
        powerPreference: 'high-performance'
      });
      if (!this.gl) throw new Error('WebGL is unavailable');
      this.program = this.createProgram();
      this.positionBuffer = this.gl.createBuffer();
      this.normalBuffer = this.gl.createBuffer();
      if (!this.positionBuffer || !this.normalBuffer) throw new Error('Unable to allocate WebGL buffers');
      this.attributes = {
        position: this.gl.getAttribLocation(this.program, 'a_position'),
        normal: this.gl.getAttribLocation(this.program, 'a_normal')
      };
      this.uniforms = {
        azimuth: this.getUniform('u_azimuth'),
        elevation: this.getUniform('u_elevation'),
        scale: this.getUniform('u_scale'),
        viewScale: this.getUniform('u_view_scale'),
        colour: this.getUniform('u_colour')
      };
      if (this.attributes.position < 0 || this.attributes.normal < 0) {
        throw new Error('Unable to bind WebGL mesh attributes');
      }
      this.vertexCount = 0;
      this.colour = parseHexColor('#7996B3');
      this.loadToken = 0;
      this.ready = false;
      this.contextLost = false;
      this.lastWidth = 0;
      this.lastHeight = 0;
      canvas.addEventListener('webglcontextlost', () => {
        this.contextLost = true;
        this.deactivate();
      });
    }

    static create(canvas, viewport) {
      if (!canvas || !viewport) return null;
      try {
        return new CadMeshRenderer(canvas, viewport);
      } catch (error) {
        console.warn('[CAD build replay] Interactive WebGL fallback:', error);
        return null;
      }
    }

    compileShader(type, source) {
      const shader = this.gl.createShader(type);
      if (!shader) throw new Error('Unable to create WebGL shader');
      this.gl.shaderSource(shader, source);
      this.gl.compileShader(shader);
      if (!this.gl.getShaderParameter(shader, this.gl.COMPILE_STATUS)) {
        throw new Error(this.gl.getShaderInfoLog(shader) || 'Unable to compile WebGL shader');
      }
      return shader;
    }

    createProgram() {
      const vertexShader = this.compileShader(this.gl.VERTEX_SHADER, `
        attribute vec3 a_position;
        attribute vec3 a_normal;
        uniform float u_azimuth;
        uniform float u_elevation;
        uniform float u_scale;
        uniform vec2 u_view_scale;
        varying float v_light;

        vec3 rotate_for_view(vec3 value) {
          float ca = cos(u_azimuth);
          float sa = sin(u_azimuth);
          float ce = cos(u_elevation);
          float se = sin(u_elevation);
          float x = value.x * ca - value.y * sa;
          float y = value.x * sa + value.y * ca;
          return vec3(x, -value.z * ce + y * se, y * ce + value.z * se);
        }

        void main() {
          vec3 position = rotate_for_view(a_position);
          vec3 normal = normalize(rotate_for_view(a_normal));
          vec3 key_light = normalize(vec3(-0.35, -0.50, 0.79));
          vec3 fill_light = normalize(vec3(0.62, 0.18, 0.76));
          float key = abs(dot(normal, key_light));
          float fill = abs(dot(normal, fill_light));
          v_light = 0.48 + key * 0.39 + fill * 0.13;
          gl_Position = vec4(
            position.x * u_scale * u_view_scale.x,
            position.y * u_scale * u_view_scale.y,
            -position.z * 0.22,
            1.0
          );
        }
      `);
      const fragmentShader = this.compileShader(this.gl.FRAGMENT_SHADER, `
        precision mediump float;
        uniform vec3 u_colour;
        varying float v_light;

        void main() {
          gl_FragColor = vec4(u_colour * v_light, 1.0);
        }
      `);
      const program = this.gl.createProgram();
      if (!program) throw new Error('Unable to create WebGL program');
      this.gl.attachShader(program, vertexShader);
      this.gl.attachShader(program, fragmentShader);
      this.gl.linkProgram(program);
      if (!this.gl.getProgramParameter(program, this.gl.LINK_STATUS)) {
        throw new Error(this.gl.getProgramInfoLog(program) || 'Unable to link WebGL program');
      }
      this.gl.deleteShader(vertexShader);
      this.gl.deleteShader(fragmentShader);
      return program;
    }

    getUniform(name) {
      const location = this.gl.getUniformLocation(this.program, name);
      if (location === null) throw new Error('Unable to bind ' + name);
      return location;
    }

    deactivate() {
      this.loadToken += 1;
      this.ready = false;
      this.vertexCount = 0;
      this.canvas.tabIndex = -1;
      this.canvas.classList.remove('is-ready', 'is-dragging');
      this.viewport.classList.remove('has-interactive');
    }

    async show(meshUrl, colour) {
      const token = ++this.loadToken;
      if (!meshUrl || this.contextLost) {
        this.deactivate();
        return;
      }
      try {
        let mesh = bundledMesh(meshUrl);
        if (!mesh) {
          const response = await fetch(meshUrl, { cache: 'force-cache' });
          if (!response.ok) throw new Error('Unable to load mesh (' + response.status + ')');
          mesh = await response.json();
        }
        if (token !== this.loadToken) return;
        this.upload(mesh);
        this.colour = parseHexColor(colour);
        this.ready = true;
        this.canvas.tabIndex = 0;
        this.canvas.classList.add('is-ready');
        this.viewport.classList.add('has-interactive');
      } catch (error) {
        if (token !== this.loadToken) return;
        this.deactivate();
        console.warn('[CAD build replay] Mesh fallback:', error);
      }
    }

    upload(mesh) {
      if (!mesh || !Array.isArray(mesh.vertices) || !Array.isArray(mesh.triangles)) {
        throw new Error('Invalid mesh data');
      }
      const positions = [];
      const normals = [];
      mesh.triangles.forEach((indices) => {
        if (!Array.isArray(indices) || indices.length < 3) return;
        const a = mesh.vertices[indices[0]];
        const b = mesh.vertices[indices[1]];
        const c = mesh.vertices[indices[2]];
        if (!a || !b || !c) return;
        const ab = [b[0] - a[0], b[1] - a[1], b[2] - a[2]];
        const ac = [c[0] - a[0], c[1] - a[1], c[2] - a[2]];
        const normal = [
          ab[1] * ac[2] - ab[2] * ac[1],
          ab[2] * ac[0] - ab[0] * ac[2],
          ab[0] * ac[1] - ab[1] * ac[0]
        ];
        const length = Math.hypot(normal[0], normal[1], normal[2]) || 1;
        const unit = normal.map((value) => value / length);
        [a, b, c].forEach((vertex) => {
          positions.push(Number(vertex[0]), Number(vertex[1]), Number(vertex[2]));
          normals.push(unit[0], unit[1], unit[2]);
        });
      });
      if (!positions.length) throw new Error('Mesh contains no triangles');
      this.gl.useProgram(this.program);
      this.gl.bindBuffer(this.gl.ARRAY_BUFFER, this.positionBuffer);
      this.gl.bufferData(this.gl.ARRAY_BUFFER, new Float32Array(positions), this.gl.STATIC_DRAW);
      this.gl.enableVertexAttribArray(this.attributes.position);
      this.gl.vertexAttribPointer(this.attributes.position, 3, this.gl.FLOAT, false, 0, 0);
      this.gl.bindBuffer(this.gl.ARRAY_BUFFER, this.normalBuffer);
      this.gl.bufferData(this.gl.ARRAY_BUFFER, new Float32Array(normals), this.gl.STATIC_DRAW);
      this.gl.enableVertexAttribArray(this.attributes.normal);
      this.gl.vertexAttribPointer(this.attributes.normal, 3, this.gl.FLOAT, false, 0, 0);
      this.vertexCount = positions.length / 3;
    }

    resize() {
      const ratio = Math.min(2, window.devicePixelRatio || 1);
      const width = Math.max(1, Math.round(this.canvas.clientWidth * ratio));
      const height = Math.max(1, Math.round(this.canvas.clientHeight * ratio));
      if (width === this.lastWidth && height === this.lastHeight) return;
      this.canvas.width = width;
      this.canvas.height = height;
      this.lastWidth = width;
      this.lastHeight = height;
      this.gl.viewport(0, 0, width, height);
    }

    render(azimuth, elevation) {
      if (!this.ready || !this.vertexCount) return;
      this.resize();
      const width = Math.max(1, this.canvas.width);
      const height = Math.max(1, this.canvas.height);
      const aspect = width / height;
      const viewScale = aspect >= 1 ? [1 / aspect, 1] : [1, aspect];
      this.gl.clearColor(0, 0, 0, 0);
      this.gl.clear(this.gl.COLOR_BUFFER_BIT | this.gl.DEPTH_BUFFER_BIT);
      this.gl.enable(this.gl.DEPTH_TEST);
      this.gl.depthFunc(this.gl.LEQUAL);
      this.gl.disable(this.gl.BLEND);
      this.gl.disable(this.gl.CULL_FACE);
      this.gl.useProgram(this.program);
      this.gl.bindBuffer(this.gl.ARRAY_BUFFER, this.positionBuffer);
      this.gl.enableVertexAttribArray(this.attributes.position);
      this.gl.vertexAttribPointer(this.attributes.position, 3, this.gl.FLOAT, false, 0, 0);
      this.gl.bindBuffer(this.gl.ARRAY_BUFFER, this.normalBuffer);
      this.gl.enableVertexAttribArray(this.attributes.normal);
      this.gl.vertexAttribPointer(this.attributes.normal, 3, this.gl.FLOAT, false, 0, 0);
      this.gl.uniform1f(this.uniforms.azimuth, azimuth);
      this.gl.uniform1f(this.uniforms.elevation, elevation);
      this.gl.uniform1f(this.uniforms.scale, 0.73);
      this.gl.uniform2f(this.uniforms.viewScale, viewScale[0], viewScale[1]);
      this.gl.uniform3f(this.uniforms.colour, this.colour[0], this.colour[1], this.colour[2]);
      this.gl.drawArrays(this.gl.TRIANGLES, 0, this.vertexCount);
    }
  }

  class CadBuildReplay {
    constructor(root) {
      this.root = root;
      this.section = root.closest('.cad-replay') || root;
      this.elements = {
        drawing: root.querySelector('[data-cad-drawing]'),
        drawingPlaceholder: root.querySelector('[data-cad-drawing-placeholder]'),
        drawingType: root.querySelector('[data-cad-drawing-type]'),
        scale: root.querySelector('[data-cad-scale]'),
        frameA: root.querySelector('[data-cad-model-frame-a]'),
        frameB: root.querySelector('[data-cad-model-frame-b]'),
        modelViewport: root.querySelector('.cad-model-viewport'),
        modelStack: root.querySelector('[data-cad-model-stack]'),
        modelLoading: root.querySelector('[data-cad-model-loading]'),
        remotionVideo: root.querySelector('[data-cad-remotion-video]'),
        interactiveCanvas: root.querySelector('[data-cad-interactive-canvas]'),
        stepCounter: root.querySelector('[data-cad-step-counter]'),
        stepLabel: root.querySelector('[data-cad-step-label]'),
        stepDetail: root.querySelector('[data-cad-step-detail]'),
        partId: root.querySelector('[data-cad-part-id]'),
        codeFile: root.querySelector('[data-cad-code-file]'),
        codeViewport: root.querySelector('[data-cad-code-viewport]'),
        codeLines: root.querySelector('[data-cad-code-lines]'),
        lineReadout: root.querySelector('[data-cad-line-readout]'),
        prev: this.section.querySelector('[data-cad-prev]'),
        toggle: this.section.querySelector('[data-cad-toggle]'),
        next: this.section.querySelector('[data-cad-next]'),
        playIcon: this.section.querySelector('[data-cad-play-icon]'),
        partCount: this.section.querySelector('[data-cad-part-count]'),
        playState: this.section.querySelector('[data-cad-play-state]'),
        liveStatus: this.section.querySelector('[data-cad-live-status]'),
        liveLabel: this.section.querySelector('[data-cad-live-label]'),
        progressBar: this.section.querySelector('[data-cad-progress-bar]'),
        partRail: this.section.querySelector('[data-cad-part-rail]'),
        liveRegion: this.section.querySelector('[data-cad-live-region]')
      };
      this.parts = [];
      this.partIndex = 0;
      this.stepIndex = 0;
      this.activeFrame = 'a';
      this.elapsed = 0;
      this.framePending = false;
      this.usingVideo = false;
      this.videoReady = false;
      this.videoToken = 0;
      this.lastTick = performance.now();
      this.inView = false;
      this.reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      this.wantsPlayback = true;
      this.codeRows = [];
      this.raf = 0;
      this.modelRenderer = CadMeshRenderer.create(this.elements.interactiveCanvas, this.elements.modelViewport);
      this.modelAzimuth = -Math.PI * 0.28;
      this.modelElevation = Math.PI * 0.145;
      this.modelDragging = false;
      this.dragPointerId = null;
      this.dragX = 0;
      this.dragY = 0;
      this.modelAutoResumeAt = 0;
    }

    async init() {
      this.bindEvents();
      this.observeVisibility();
      let manifest = window.CAD_BUILD_MANIFEST;
      if (!manifest) {
        const response = await fetch(MANIFEST_URL, { cache: 'no-store' });
        if (!response.ok) throw new Error('Unable to load reconstruction manifest (' + response.status + ')');
        manifest = await response.json();
      }
      const rawParts = Array.isArray(manifest) ? manifest : manifest.parts;
      if (!rawParts || !rawParts.length) throw new Error('The reconstruction manifest contains no parts.');
      this.parts = await Promise.all(rawParts.map((part, index) => (
        normalisePart(part, index, manifest.defaultStepDurationMs)
      )));
      this.renderPartRail();
      this.showPart(0, true);
      this.root.setAttribute('aria-busy', 'false');
      [this.elements.prev, this.elements.toggle, this.elements.next].filter(Boolean).forEach((button) => {
        button.disabled = false;
      });
      this.updatePlaybackUi();
      this.tick(performance.now());
    }

    bindEvents() {
      this.bindModelInteraction();
      if (this.elements.prev) this.elements.prev.addEventListener('click', () => this.previousStep());
      if (this.elements.next) this.elements.next.addEventListener('click', () => this.nextStep(true));
      if (this.elements.toggle) {
        this.elements.toggle.addEventListener('click', () => {
          this.wantsPlayback = !this.wantsPlayback;
          this.lastTick = performance.now();
          this.updatePlaybackUi();
          this.syncVideoPlayback();
        });
      }

      this.section.addEventListener('keydown', (event) => {
        if (event.target && event.target.closest && event.target.closest('.cad-code-viewport')) return;
        if (event.target && event.target.closest && event.target.closest('.cad-interactive-canvas')) return;
        if (event.key === 'ArrowLeft') {
          event.preventDefault();
          this.previousStep();
        } else if (event.key === 'ArrowRight') {
          event.preventDefault();
          this.nextStep(true);
        }
      });

      document.addEventListener('visibilitychange', () => {
        this.lastTick = performance.now();
        this.syncVideoPlayback();
      });
    }

    bindModelInteraction() {
      const canvas = this.elements.interactiveCanvas;
      const surface = this.elements.modelViewport || canvas;
      if (!canvas || !surface || !this.modelRenderer) return;

      const resumeAfterDrag = (settled) => {
        const bounds = this.section.getBoundingClientRect();
        this.inView = bounds.bottom > 0
          && bounds.right > 0
          && bounds.top < window.innerHeight
          && bounds.left < window.innerWidth;
        this.lastTick = performance.now();
        this.syncVideoPlayback();
        if (!settled) window.setTimeout(() => resumeAfterDrag(true), 120);
      };

      const finishDrag = (event) => {
        if (!this.modelDragging || (event && event.pointerId !== this.dragPointerId)) return;
        if (event && surface.hasPointerCapture && surface.hasPointerCapture(event.pointerId)) {
          surface.releasePointerCapture(event.pointerId);
        }
        this.modelDragging = false;
        this.dragPointerId = null;
        this.modelAutoResumeAt = performance.now() + 600;
        canvas.classList.remove('is-dragging');
        surface.classList.remove('is-dragging');
        resumeAfterDrag();
      };

      surface.addEventListener('pointerdown', (event) => {
        if (event.pointerType === 'mouse' && event.button !== 0) return;
        event.preventDefault();
        canvas.focus();
        this.modelDragging = true;
        this.modelAutoResumeAt = Number.POSITIVE_INFINITY;
        this.dragPointerId = event.pointerId;
        this.dragX = event.clientX;
        this.dragY = event.clientY;
        canvas.classList.add('is-dragging');
        surface.classList.add('is-dragging');
        if (surface.setPointerCapture) surface.setPointerCapture(event.pointerId);
      });

      surface.addEventListener('pointermove', (event) => {
        if (!this.modelDragging || event.pointerId !== this.dragPointerId) return;
        event.preventDefault();
        const deltaX = event.clientX - this.dragX;
        const deltaY = event.clientY - this.dragY;
        this.dragX = event.clientX;
        this.dragY = event.clientY;
        this.modelAzimuth += deltaX * 0.009;
        this.modelElevation = clamp(
          this.modelElevation - deltaY * 0.007,
          -Math.PI * 0.38,
          Math.PI * 0.38
        );
        surface.dataset.userRotated = 'true';
      });

      surface.addEventListener('pointerup', finishDrag);
      surface.addEventListener('pointercancel', finishDrag);
      surface.addEventListener('lostpointercapture', () => {
        if (!this.modelDragging) return;
        this.modelDragging = false;
        this.dragPointerId = null;
        this.modelAutoResumeAt = performance.now() + 600;
        canvas.classList.remove('is-dragging');
        surface.classList.remove('is-dragging');
        resumeAfterDrag();
      });
      surface.addEventListener('contextmenu', (event) => event.preventDefault());
      canvas.addEventListener('keydown', (event) => {
        const amount = event.shiftKey ? 0.18 : 0.09;
        if (event.key === 'ArrowLeft') this.modelAzimuth -= amount;
        else if (event.key === 'ArrowRight') this.modelAzimuth += amount;
        else if (event.key === 'ArrowUp') {
          this.modelElevation = clamp(this.modelElevation + amount, -Math.PI * 0.38, Math.PI * 0.38);
        } else if (event.key === 'ArrowDown') {
          this.modelElevation = clamp(this.modelElevation - amount, -Math.PI * 0.38, Math.PI * 0.38);
        } else {
          return;
        }
        event.preventDefault();
        event.stopPropagation();
      });
    }

    observeVisibility() {
      if (!('IntersectionObserver' in window)) {
        this.inView = true;
        return;
      }
      const observer = new IntersectionObserver((entries) => {
        this.inView = Boolean(entries[0] && entries[0].isIntersecting);
        this.lastTick = performance.now();
        this.syncVideoPlayback();
      }, { threshold: 0.16 });
      observer.observe(this.section);
    }

    renderPartRail() {
      if (!this.elements.partRail) return;
      const fragment = document.createDocumentFragment();
      this.parts.forEach((part, index) => {
        const button = document.createElement('button');
        button.type = 'button';
        button.className = 'cad-part-button';
        button.textContent = String(index + 1).padStart(2, '0');
        button.setAttribute('aria-label', 'Show part ' + (index + 1) + ': ' + part.id);
        button.addEventListener('click', () => {
          this.showPart(index, false, true);
          this.updatePlaybackUi();
        });
        fragment.appendChild(button);
      });
      this.elements.partRail.replaceChildren(fragment);
    }

    showPart(index, initial, shouldAnnounce) {
      this.disableRemotionVideo();
      this.partIndex = (index + this.parts.length) % this.parts.length;
      this.stepIndex = 0;
      this.elapsed = 0;
      const part = this.parts[this.partIndex];

      if (this.elements.partId) this.elements.partId.textContent = part.id;
      if (this.elements.codeFile) this.elements.codeFile.textContent = part.codeFile;
      if (this.elements.drawingType) this.elements.drawingType.textContent = part.drawingType;
      if (this.elements.scale) this.elements.scale.textContent = part.scale;
      if (this.elements.partCount) this.elements.partCount.textContent = 'PART ' + String(this.partIndex + 1).padStart(2, '0') + ' / ' + String(this.parts.length).padStart(2, '0');
      this.renderCode(part.sourceCode);
      this.setDrawing(part);
      this.updatePartRail();
      this.showStep(0, initial, shouldAnnounce);
      this.setupRemotionVideo(part);
      this.preloadUpcoming();
    }

    setDrawing(part) {
      const image = this.elements.drawing;
      if (!image) return;
      image.classList.remove('is-ready');
      if (this.elements.drawingPlaceholder) this.elements.drawingPlaceholder.classList.remove('is-hidden');
      image.alt = 'Engineering drawing for part ' + part.id;
      image.onload = () => {
        image.classList.add('is-ready');
        if (this.elements.drawingPlaceholder) this.elements.drawingPlaceholder.classList.add('is-hidden');
      };
      image.onerror = () => {
        image.classList.remove('is-ready');
      };
      image.src = part.drawing;
    }

    disableRemotionVideo() {
      const video = this.elements.remotionVideo;
      this.videoToken += 1;
      this.usingVideo = false;
      this.videoReady = false;
      if (!video) return;
      video.onloadeddata = null;
      video.onerror = null;
      video.onended = null;
      video.pause();
      video.classList.remove('is-active');
      if (this.elements.modelViewport) this.elements.modelViewport.classList.remove('has-remotion');
      if (video.hasAttribute('src')) {
        video.removeAttribute('src');
        video.load();
      }
    }

    setupRemotionVideo(part) {
      const video = this.elements.remotionVideo;
      if (!video || this.reducedMotion || !part.remotion || !part.remotion.animation) return;

      const token = ++this.videoToken;
      this.usingVideo = true;
      this.videoReady = false;
      video.setAttribute('aria-label', 'Remotion build animation for part ' + part.id);
      video.onloadeddata = () => {
        if (token !== this.videoToken) return;
        this.videoReady = true;
        this.framePending = false;
        this.lastTick = performance.now();
        video.classList.add('is-active');
        if (this.elements.modelViewport) this.elements.modelViewport.classList.add('has-remotion');
        if (this.elements.modelLoading) this.elements.modelLoading.classList.add('is-hidden');
        this.syncVideoPlayback();
      };
      video.onerror = () => {
        if (token !== this.videoToken) return;
        this.disableRemotionVideo();
        this.lastTick = performance.now();
      };
      video.onended = () => {
        if (token !== this.videoToken) return;
        this.showPart(this.partIndex + 1, false, false);
      };
      video.src = part.remotion.animation;
      video.load();
    }

    syncVideoPlayback() {
      const video = this.elements.remotionVideo;
      if (!video || !this.usingVideo || !this.videoReady) return;
      if (this.isPlaying()) {
        video.play().catch(() => {
          this.disableRemotionVideo();
          this.lastTick = performance.now();
        });
      } else if (!video.paused) {
        video.pause();
      }
    }

    videoStepState(part, timeMs) {
      let cursor = 0;
      for (let index = 0; index < part.steps.length; index += 1) {
        const step = part.steps[index];
        const hold = index === part.steps.length - 1 && part.remotion
          ? part.remotion.finalHoldMs
          : 0;
        const duration = Math.max(1, step.videoDuration + hold);
        if (timeMs < cursor + duration || index === part.steps.length - 1) {
          return { index: index, progress: clamp((timeMs - cursor) / duration, 0, 1) };
        }
        cursor += duration;
      }
      return { index: part.steps.length - 1, progress: 1 };
    }

    videoStartForStep(part, targetIndex) {
      return part.steps.slice(0, targetIndex).reduce((total, step) => total + step.videoDuration, 0);
    }

    seekVideoStep(targetIndex, shouldAnnounce) {
      const part = this.parts[this.partIndex];
      const boundedIndex = clamp(targetIndex, 0, part.steps.length - 1);
      const video = this.elements.remotionVideo;
      if (this.usingVideo && this.videoReady) {
        video.currentTime = this.videoStartForStep(part, boundedIndex) / 1000;
      }
      this.showStep(boundedIndex, false, shouldAnnounce, true);
      this.syncVideoPlayback();
    }

    renderCode(source) {
      if (!this.elements.codeLines) return;
      const fragment = document.createDocumentFragment();
      this.codeRows = prepareCodeForDisplay(source);
      this.codeRows.forEach((row) => {
        const lineElement = document.createElement('span');
        lineElement.className = 'cad-code-line';
        lineElement.dataset.line = String(row.sourceLine);
        lineElement.dataset.sourceLine = String(row.sourceLine);
        lineElement.innerHTML = syntaxLine(row.text);
        fragment.appendChild(lineElement);
      });
      this.elements.codeLines.replaceChildren(fragment);
      if (this.elements.codeViewport) this.elements.codeViewport.scrollTop = 0;
    }

    showStep(index, initial, shouldAnnounce, fromVideo) {
      const part = this.parts[this.partIndex];
      this.stepIndex = clamp(index, 0, part.steps.length - 1);
      this.elapsed = 0;
      const step = part.steps[this.stepIndex];

      if (this.elements.stepCounter) this.elements.stepCounter.textContent = 'STEP ' + String(this.stepIndex + 1).padStart(2, '0') + ' / ' + String(part.steps.length).padStart(2, '0');
      if (this.elements.stepLabel) this.elements.stepLabel.textContent = step.label;
      if (this.elements.stepDetail) this.elements.stepDetail.textContent = step.detail;
      if (this.elements.lineReadout) {
        this.elements.lineReadout.textContent = step.lineStart === step.lineEnd
          ? 'Ln ' + step.lineStart
          : 'Ln ' + step.lineStart + '–' + step.lineEnd;
      }
      if (!fromVideo) this.setFrame(step.frame, initial);
      if (this.modelRenderer) this.modelRenderer.show(step.mesh, part.modelColor);
      this.highlightCode(step.lineStart, step.lineEnd, initial);
      if (shouldAnnounce) this.announce(part, step);
      this.updateProgress(0);
      this.preloadUpcoming();
    }

    setFrame(src, initial) {
      if (!src) {
        this.framePending = false;
        return;
      }
      const current = this.activeFrame === 'a' ? this.elements.frameA : this.elements.frameB;
      const next = this.activeFrame === 'a' ? this.elements.frameB : this.elements.frameA;
      if (!current || !next) {
        this.framePending = false;
        return;
      }
      this.framePending = true;
      let revealed = false;
      const reveal = () => {
        if (revealed) return;
        revealed = true;
        this.framePending = false;
        this.lastTick = performance.now();
        if (this.elements.modelLoading) this.elements.modelLoading.classList.add('is-hidden');
        if (initial && !current.src) {
          current.src = src;
          current.classList.add('is-visible');
          return;
        }
        next.classList.add('is-visible');
        current.classList.remove('is-visible');
        this.activeFrame = this.activeFrame === 'a' ? 'b' : 'a';
        if (this.elements.modelStack) {
          this.elements.modelStack.classList.remove('is-switching');
          void this.elements.modelStack.offsetWidth;
          this.elements.modelStack.classList.add('is-switching');
        }
      };

      if (current.src === new URL(src, document.baseURI).href) {
        current.classList.add('is-visible');
        if (this.elements.modelLoading) this.elements.modelLoading.classList.add('is-hidden');
        this.framePending = false;
        return;
      }

      next.onload = reveal;
      next.onerror = () => {
        this.framePending = false;
        this.lastTick = performance.now();
        if (this.elements.modelLoading) {
          this.elements.modelLoading.classList.remove('is-hidden');
        }
      };
      next.src = src;
      if (next.complete && next.naturalWidth) reveal();
    }

    highlightCode(startLine, endLine, initial) {
      if (!this.elements.codeLines) return;
      const lines = Array.from(this.elements.codeLines.querySelectorAll('.cad-code-line'));
      if (!lines.length) return;
      const start = Math.min(startLine, endLine);
      const end = Math.max(startLine, endLine);
      let activeLines = lines.filter((line) => {
        const sourceLine = Number(line.dataset.sourceLine);
        return sourceLine >= start && sourceLine <= end;
      });
      if (!activeLines.length) {
        activeLines = [lines.reduce((nearest, line) => {
          const sourceLine = Number(line.dataset.sourceLine);
          const distance = sourceLine < start ? start - sourceLine : sourceLine - end;
          if (!nearest || distance < nearest.distance) return { line: line, distance: distance };
          return nearest;
        }, null).line];
      }
      const activeSet = new Set(activeLines);
      let firstActive = null;
      lines.forEach((line) => {
        const active = activeSet.has(line);
        line.classList.toggle('is-active', active);
        if (active && !firstActive) firstActive = line;
      });
      if (firstActive && this.elements.codeViewport) {
        const targetTop = Math.max(0, firstActive.offsetTop - this.elements.codeViewport.clientHeight * 0.34);
        this.elements.codeViewport.scrollTo({
          top: targetTop,
          behavior: initial || this.reducedMotion ? 'auto' : 'smooth'
        });
      }
    }

    updatePartRail() {
      if (!this.elements.partRail) return;
      Array.from(this.elements.partRail.children).forEach((button, index) => {
        const active = index === this.partIndex;
        button.classList.toggle('is-active', active);
        if (active) button.setAttribute('aria-current', 'true');
        else button.removeAttribute('aria-current');
      });
    }

    updatePlaybackUi() {
      const paused = !this.wantsPlayback;
      if (this.elements.playIcon) this.elements.playIcon.className = 'cad-toggle-glyph ' + (paused ? 'is-play' : 'is-pause');
      if (this.elements.toggle) {
        this.elements.toggle.setAttribute('aria-label', paused ? 'Play build replay' : 'Pause build replay');
        this.elements.toggle.title = paused ? 'Play replay' : 'Pause replay';
      }
      if (this.elements.playState) {
        this.elements.playState.textContent = this.reducedMotion
          ? (paused ? 'MANUAL · REDUCED MOTION' : 'PLAYING')
          : (paused ? 'PAUSED' : 'AUTO LOOP');
      }
      if (this.elements.liveStatus && this.elements.liveLabel) {
        this.elements.liveStatus.classList.toggle('is-live', !paused);
        this.elements.liveStatus.classList.toggle('is-paused', paused);
        this.elements.liveLabel.textContent = paused ? 'Paused' : 'Live replay';
      }
    }

    updateProgress(progress) {
      if (this.elements.progressBar) this.elements.progressBar.style.width = (clamp(progress, 0, 1) * 100).toFixed(2) + '%';
    }

    isPlaying() {
      return this.wantsPlayback && this.inView && !document.hidden;
    }

    nextStep(manual) {
      if (!this.parts.length) return;
      if (this.usingVideo && !this.videoReady) this.disableRemotionVideo();
      const part = this.parts[this.partIndex];
      if (this.usingVideo && this.videoReady) {
        if (this.stepIndex < part.steps.length - 1) {
          this.seekVideoStep(this.stepIndex + 1, manual);
        } else {
          this.showPart(this.partIndex + 1, false, manual);
        }
        if (manual) this.lastTick = performance.now();
        return;
      }
      if (this.stepIndex < part.steps.length - 1) {
        this.showStep(this.stepIndex + 1, false, manual);
      } else {
        this.showPart(this.partIndex + 1, false, manual);
      }
      if (manual) this.lastTick = performance.now();
    }

    previousStep() {
      if (!this.parts.length) return;
      if (this.usingVideo && !this.videoReady) this.disableRemotionVideo();
      if (this.usingVideo && this.videoReady) {
        if (this.stepIndex > 0) {
          this.seekVideoStep(this.stepIndex - 1, true);
        } else {
          const previousPart = (this.partIndex - 1 + this.parts.length) % this.parts.length;
          this.showPart(previousPart, false, false);
          const lastStep = this.parts[previousPart].steps.length - 1;
          const activateLastStep = () => {
            if (this.partIndex !== previousPart) return;
            if (this.usingVideo && this.videoReady) this.seekVideoStep(lastStep, true);
            else this.showStep(lastStep, false, true);
          };
          if (this.usingVideo) {
            this.elements.remotionVideo.addEventListener('loadeddata', activateLastStep, { once: true });
          } else {
            activateLastStep();
          }
        }
        this.lastTick = performance.now();
        return;
      }
      if (this.stepIndex > 0) {
        this.showStep(this.stepIndex - 1, false, true);
      } else {
        const previousPart = (this.partIndex - 1 + this.parts.length) % this.parts.length;
        this.showPart(previousPart, false, false);
        const lastStep = this.parts[previousPart].steps.length - 1;
        this.showStep(lastStep, false, true);
      }
      this.lastTick = performance.now();
    }

    tick(now) {
      const delta = Math.min(120, Math.max(0, now - this.lastTick));
      this.lastTick = now;
      if (this.modelRenderer && this.modelRenderer.ready) {
        if (this.isPlaying() && !this.modelDragging && now >= this.modelAutoResumeAt && !this.reducedMotion) {
          this.modelAzimuth += (delta / AUTO_ROTATION_PERIOD_MS) * Math.PI * 2;
          if (Math.abs(this.modelAzimuth) > Math.PI * 4) this.modelAzimuth %= Math.PI * 2;
        }
        this.modelRenderer.render(this.modelAzimuth, this.modelElevation);
      }
      if (this.parts.length && this.usingVideo) {
        if (this.videoReady) {
          const video = this.elements.remotionVideo;
          const part = this.parts[this.partIndex];
          const state = this.videoStepState(part, video.currentTime * 1000);
          if (state.index !== this.stepIndex) this.showStep(state.index, false, false, true);
          const duration = Number.isFinite(video.duration) && video.duration > 0
            ? video.duration
            : ((part.remotion && part.remotion.durationMs) || 1) / 1000;
          this.updateProgress(video.currentTime / duration);
        }
        this.raf = requestAnimationFrame((time) => this.tick(time));
        return;
      }
      if (this.parts.length && this.isPlaying() && !this.framePending) {
        const step = this.parts[this.partIndex].steps[this.stepIndex];
        this.elapsed += delta;
        this.updateProgress(this.elapsed / step.duration);
        if (this.elapsed >= step.duration) this.nextStep(false);
      }
      this.raf = requestAnimationFrame((time) => this.tick(time));
    }

    preloadUpcoming() {
      if (!this.parts.length) return;
      const part = this.parts[this.partIndex];
      const nextStep = part.steps[this.stepIndex + 1];
      const nextPart = this.parts[(this.partIndex + 1) % this.parts.length];
      [nextStep && nextStep.frame, nextPart && nextPart.drawing, nextPart && nextPart.steps[0] && nextPart.steps[0].frame]
        .filter(Boolean)
        .forEach((src) => {
          const image = new Image();
          image.src = src;
        });
    }

    announce(part, step) {
      if (this.elements.liveRegion) this.elements.liveRegion.textContent = 'Part ' + (this.partIndex + 1) + ' of ' + this.parts.length + ', ' + part.id + '. ' + step.label + '.';
    }

    showError(error) {
      console.error('[CAD build replay]', error);
      this.section.classList.add('has-error');
      this.root.setAttribute('aria-busy', 'false');
      if (this.elements.codeLines) this.elements.codeLines.replaceChildren();
    }
  }

  function start() {
    const root = document.querySelector('[data-cad-replay]');
    if (!root) return;
    const replay = new CadBuildReplay(root);
    replay.init().catch((error) => replay.showError(error));
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start, { once: true });
  else start();
})();
